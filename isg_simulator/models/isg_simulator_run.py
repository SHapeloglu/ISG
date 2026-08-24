# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime

class IsgSimulatorRun(models.Model):
    _name = 'isg.simulator.run'
    _description = 'İSG Müfettiş Simülasyonu'
    _inherit = 'isg.uuid.mixin'
    _order = 'run_date desc'
    _rec_name = 'sequence'

    # Temel Alanlar
    sequence = fields.Char(
        string='Simülasyon No',
        default='/',
        readonly=True,
        copy=False,
        index=True
    )
    workplace_id = fields.Many2one(
        'isg.workplace',
        string='İşyeri',
        required=True,
        ondelete='cascade',
        readonly=False
    )
    company_id = fields.Many2one(
        'res.company',
        string='Şirket',
        related='workplace_id.company_id',
        store=True,
        readonly=True
    )
    run_date = fields.Datetime(
        string='Simülasyon Tarihi',
        default=lambda self: datetime.now(),
        readonly=False
    )
    evaluator_id = fields.Many2one(
        'res.users',
        string='Değerlendirenin Kullanıcısı',
        default=lambda self: self.env.user,
        readonly=True
    )
    state = fields.Selection(
        [
            ('draft', 'Taslak'),
            ('completed', 'Tamamlandı'),
        ],
        string='Durum',
        default='draft',
        readonly=True
    )

    # Hesaplı Alanlar (Snapshot)
    total_penalty_amount = fields.Float(
        string='Tahmini Toplam Ceza',
        compute='_compute_totals',
        store=True,
        readonly=True
    )
    compliance_rate = fields.Float(
        string='Uygunluk Oranı (%)',
        compute='_compute_totals',
        store=True,
        readonly=True
    )
    risk_level = fields.Selection(
        [
            ('low', 'Düşük'),
            ('medium', 'Orta'),
            ('high', 'Yüksek'),
        ],
        string='Risk Seviyesi',
        compute='_compute_totals',
        store=True,
        readonly=True
    )

    # Finding Satırları
    finding_ids = fields.One2many(
        'isg.simulator.finding',
        'run_id',
        string='Bulgular',
        readonly=False
    )

    # Memo
    notes = fields.Text(
        string='Notlar',
        readonly=False
    )

    @api.model
    def create(self, vals):
        if vals.get('sequence', '/') == '/':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('isg.simulator.run') or '/'
        return super().create(vals)

    @api.depends('finding_ids.estimated_penalty_amount', 'finding_ids.compliance_status')
    def _compute_totals(self):
        """Toplam ceza, uygunluk oranı ve risk seviyesi hesapla"""
        for record in self:
            # Toplam ceza
            record.total_penalty_amount = sum(
                finding.estimated_penalty_amount 
                for finding in record.finding_ids
            )

            # Uygunluk oranı
            total_findings = len(record.finding_ids)
            if total_findings > 0:
                compliant_count = len(
                    record.finding_ids.filtered(
                        lambda f: f.compliance_status == 'compliant'
                    )
                )
                record.compliance_rate = (compliant_count / total_findings) * 100
            else:
                record.compliance_rate = 0.0

            # Risk seviyesi
            if record.compliance_rate >= 90:
                record.risk_level = 'low'
            elif record.compliance_rate >= 70:
                record.risk_level = 'medium'
            else:
                record.risk_level = 'high'

    def action_run_simulation(self):
        """Simülasyon çalıştır: workplace için tüm yükümlülükleri değerlendir"""
        self.ensure_one()

        if self.state != 'draft':
            raise models.ValidationError('Simülasyon sadece Taslak durumda çalıştırılabilir.')

        # Mevcut finding'leri temizle (yeniden çalıştırma durumunda)
        self.finding_ids.unlink()

        # Workplace'in tehlike sınıfını ve çalışan sayısını al
        workplace = self.workplace_id
        danger_class = workplace.danger_class

        # Uygulanabilir yükümlülükleri bul
        applicable_obligations = self.env['isg.obligation'].search([
            ('danger_classes', 'ilike', danger_class),
        ])

        # Her yükümlülük için finding satırı oluştur
        for obligation in applicable_obligations:
            # Mevcut compliance durumunu kontrol et
            compliance = self.env['isg.compliance'].search(
                [
                    ('workplace_id', '=', workplace.id),
                    ('obligation_id', '=', obligation.id),
                ],
                limit=1,
                order='evaluation_date desc'
            )

            if compliance:
                compliance_status = compliance.status
                # Penalty hesapla, eğer uygun değilse
                if compliance_status != 'compliant':
                    estimated_penalty = self._estimate_penalty(obligation, workplace)
                else:
                    estimated_penalty = 0.0
            else:
                # Hiç değerlendirilmemiş = eksik
                compliance_status = 'non_compliant'
                estimated_penalty = self._estimate_penalty(obligation, workplace)

            # Severity belirle
            severity = self._determine_severity(compliance_status)
            recommendation = self._generate_recommendation(obligation, compliance_status)

            # Finding satırı oluştur
            self.env['isg.simulator.finding'].create({
                'run_id': self.id,
                'obligation_id': obligation.id,
                'compliance_status': compliance_status,
                'estimated_penalty_amount': estimated_penalty,
                'severity': severity,
                'recommendation': recommendation,
            })

        # Durum tamamlandı olarak işaretle
        self.state = 'completed'

    def _estimate_penalty(self, obligation, workplace):
        """Yükümlülüğün çiğnenmesi halinde tahmini ceza hesapla"""
        # evidence_type'tan tarife bul
        penalty_tariff = self.env['isg.penalty.tariff'].search(
            [('evidence_type', '=', obligation.evidence_type)],
            limit=1
        )

        if not penalty_tariff:
            return 0.0

        # Ceza tutarını hesapla
        calculated_amount = penalty_tariff.penalty_amount
        if penalty_tariff.per_employee:
            calculated_amount *= workplace.employee_count or 1

        # Tekrar çarpanı uygulanabilirse (basit: ilk ihlal için 1x)
        calculated_amount *= 1  # Placeholder: tekrar logic'i daha sonra

        return calculated_amount

    def _determine_severity(self, compliance_status):
        """Uygunluk durumuna göre önem seviyesi belirle"""
        severity_map = {
            'compliant': 'low',
            'pending': 'medium',
            'overdue': 'high',
            'non_compliant': 'high',
        }
        return severity_map.get(compliance_status, 'medium')

    def _generate_recommendation(self, obligation, compliance_status):
        """Uygunluk durumuna göre öneri metni üret"""
        if compliance_status == 'compliant':
            return f"{obligation.name} — Uyumlu, devam gerekli"
        elif compliance_status == 'pending':
            return f"{obligation.name} — Değerlendirme beklenmede, tamamlanmalı"
        elif compliance_status == 'overdue':
            return f"{obligation.name} — Vadesi geçmiş, acil gözden geçirilmeli"
        else:
            return f"{obligation.name} — Eksik, derhal uygulanmalı"
