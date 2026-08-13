# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class IsgRiskLine(models.Model):
    _name = 'isg.risk.line'
    _description = 'Tehlike / Risk Satırı'
    _order = 'risk_score desc, id asc'

    assessment_id = fields.Many2one(
        'isg.risk.assessment', string='Risk Değerlendirmesi',
        required=True, ondelete='cascade', index=True,
    )
    method = fields.Selection(
        related='assessment_id.method', store=True,
    )
    company_id = fields.Many2one(
        related='assessment_id.company_id', store=True,
    )

    # --- Tehlike Tanımı ---
    # NOT: location_id, assessment_id.workplace_id ile aynı işyeri altında
    # olmalıdır ama alan-seviyesi domain'de ilişki zinciri (nokta ile erişim)
    # client tarafında güvenilir çalışmadığından burada kısıtlanmadı.
    # Form view'da gerekirse view-seviyesinde context/domain ile ele alınabilir.
    location_id = fields.Many2one('isg.site', string='Lokasyon')
    hazard_category = fields.Selection(
        [
            ('physical', 'Fiziksel'),
            ('chemical', 'Kimyasal'),
            ('biological', 'Biyolojik'),
            ('ergonomic', 'Ergonomik'),
            ('psychosocial', 'Psikososyal'),
            ('mechanical', 'Mekanik'),
            ('electrical', 'Elektrik'),
            ('fire_explosion', 'Yangın / Patlama'),
            ('fall', 'Düşme / Kayma'),
            ('other', 'Diğer'),
        ],
        string='Tehlike Kategorisi', required=True,
    )
    hazard_description = fields.Text(string='Tehlike Tanımı', required=True)
    affected_persons = fields.Char(string='Etkilenen Kişiler / Gruplar')
    existing_controls = fields.Text(string='Mevcut Kontrol Önlemleri')

    # --- L Matrisi Puanlama (5x5) ---
    L_SCALE_PROB = [
        ('1', '1 — Çok Düşük (Neredeyse İmkânsız)'),
        ('2', '2 — Düşük (Küçük İhtimal)'),
        ('3', '3 — Orta (Ara Sıra)'),
        ('4', '4 — Yüksek (Muhtemel)'),
        ('5', '5 — Çok Yüksek (Kaçınılmaz)'),
    ]
    L_SCALE_SEV = [
        ('1', '1 — Önemsiz (İlk Yardım)'),
        ('2', '2 — Hafif (Kayıp İş Günü Yok)'),
        ('3', '3 — Orta (Kayıp İş Günü)'),
        ('4', '4 — Ağır (Sürekli İş Göremezlik)'),
        ('5', '5 — Çok Ağır (Ölüm / Toplu Kaza)'),
    ]
    probability_l = fields.Selection(L_SCALE_PROB, string='Olasılık (L)')
    severity_l = fields.Selection(L_SCALE_SEV, string='Şiddet (L)')

    # --- Fine-Kinney Puanlama (Kinney-Wiruth standart skalası) ---
    FK_SCALE_PROB = [
        ('0.2', '0.2 — Çok Uzak İhtimal'),
        ('0.5', '0.5 — Uzak İhtimal'),
        ('1', '1 — Düşük İhtimal'),
        ('3', '3 — Olağandışı Ama Mümkün'),
        ('6', '6 — Olası'),
        ('10', '10 — Çok Olası'),
    ]
    FK_SCALE_FREQ = [
        ('0.5', '0.5 — Çok Nadir (Yılda 1)'),
        ('1', '1 — Nadir (Yılda Birkaç)'),
        ('2', '2 — Ara Sıra (Ayda 1)'),
        ('3', '3 — Düzenli (Haftada 1)'),
        ('6', '6 — Sık (Günlük)'),
        ('10', '10 — Sürekli'),
    ]
    FK_SCALE_SEV = [
        ('1', '1 — Küçük Yaralanma'),
        ('3', '3 — Önemli Yaralanma'),
        ('7', '7 — Ağır Yaralanma'),
        ('15', '15 — Tek Ölüm'),
        ('40', '40 — Birden Fazla Ölüm'),
        ('100', '100 — Felaket'),
    ]
    probability_fk = fields.Selection(FK_SCALE_PROB, string='Olasılık (FK)')
    frequency_fk = fields.Selection(FK_SCALE_FREQ, string='Frekans (FK)')
    severity_fk = fields.Selection(FK_SCALE_SEV, string='Şiddet (FK)')

    # --- Risk Skoru (compute) ---
    risk_score = fields.Float(
        string='Risk Skoru', compute='_compute_risk_score', store=True,
    )
    RISK_LEVELS = [
        ('acceptable', 'Kabul Edilebilir'),
        ('low', 'Düşük Risk'),
        ('medium', 'Orta Risk'),
        ('high', 'Yüksek Risk'),
        ('intolerable', 'Tolerans Gösterilemez'),
    ]
    risk_level = fields.Selection(
        RISK_LEVELS, string='Risk Seviyesi',
        compute='_compute_risk_score', store=True,
    )

    # --- Kontrol Önlemleri ---
    control_hierarchy = fields.Selection(
        [
            ('elimination', '1 — Ortadan Kaldırma'),
            ('substitution', '2 — İkame'),
            ('engineering', '3 — Mühendislik Kontrolü'),
            ('administrative', '4 — İdari Kontrol'),
            ('ppe', '5 — KKD'),
        ],
        string='Kontrol Hiyerarşisi',
    )
    additional_controls = fields.Text(string='Planlanan Ek Kontroller')
    responsible_id = fields.Many2one('hr.employee', string='Sorumlu')
    deadline = fields.Date(string='Termin')

    # --- Kalıntı Risk ---
    residual_probability_l = fields.Selection(L_SCALE_PROB, string='Kalıntı Olasılık (L)')
    residual_severity_l = fields.Selection(L_SCALE_SEV, string='Kalıntı Şiddet (L)')
    residual_probability_fk = fields.Selection(FK_SCALE_PROB, string='Kalıntı Olasılık (FK)')
    residual_frequency_fk = fields.Selection(FK_SCALE_FREQ, string='Kalıntı Frekans (FK)')
    residual_severity_fk = fields.Selection(FK_SCALE_SEV, string='Kalıntı Şiddet (FK)')

    residual_score = fields.Float(
        string='Kalıntı Risk Skoru', compute='_compute_residual_score', store=True,
    )
    residual_level = fields.Selection(
        RISK_LEVELS, string='Kalıntı Risk Seviyesi',
        compute='_compute_residual_score', store=True,
    )

    capa_id = fields.Many2one(
        'isg.capa', string='İlgili DÖF', readonly=True, copy=False,
    )

    # -------------------------------------------------------------------
    # Yardımcı metodlar
    # -------------------------------------------------------------------

    @staticmethod
    def _level_from_score_l(score):
        # L Matrisi 5x5: maksimum 25
        if score <= 4:
            return 'acceptable'
        elif score <= 8:
            return 'low'
        elif score <= 12:
            return 'medium'
        elif score <= 16:
            return 'high'
        else:
            return 'intolerable'

    @staticmethod
    def _level_from_score_fk(score):
        # Fine-Kinney standart (Kinney-Wiruth) bantları
        if score < 20:
            return 'acceptable'
        elif score < 70:
            return 'low'
        elif score < 200:
            return 'medium'
        elif score < 400:
            return 'high'
        else:
            return 'intolerable'

    # -------------------------------------------------------------------
    # Compute
    # -------------------------------------------------------------------

    @api.depends(
        'method', 'probability_l', 'severity_l',
        'probability_fk', 'frequency_fk', 'severity_fk',
    )
    def _compute_risk_score(self):
        for rec in self:
            if rec.method == 'l_matrix':
                p = int(rec.probability_l or 0)
                s = int(rec.severity_l or 0)
                score = p * s
                rec.risk_score = score
                rec.risk_level = rec._level_from_score_l(score) if score else False
            else:
                p = float(rec.probability_fk or 0)
                f = float(rec.frequency_fk or 0)
                s = float(rec.severity_fk or 0)
                score = p * f * s
                rec.risk_score = score
                rec.risk_level = rec._level_from_score_fk(score) if score else False

    @api.depends(
        'method',
        'residual_probability_l', 'residual_severity_l',
        'residual_probability_fk', 'residual_frequency_fk', 'residual_severity_fk',
    )
    def _compute_residual_score(self):
        for rec in self:
            if rec.method == 'l_matrix':
                p = int(rec.residual_probability_l or 0)
                s = int(rec.residual_severity_l or 0)
                score = p * s
                rec.residual_score = score
                rec.residual_level = rec._level_from_score_l(score) if score else False
            else:
                p = float(rec.residual_probability_fk or 0)
                f = float(rec.residual_frequency_fk or 0)
                s = float(rec.residual_severity_fk or 0)
                score = p * f * s
                rec.residual_score = score
                rec.residual_level = rec._level_from_score_fk(score) if score else False

    # -------------------------------------------------------------------
    # Yüksek risk -> DÖF
    # -------------------------------------------------------------------

    def action_create_capa(self):
        self.ensure_one()
        if self.capa_id:
            raise UserError(
                'Bu satır için zaten bir DÖF kaydı mevcut: %s' % self.capa_id.name
            )
        if self.risk_level not in ('high', 'intolerable'):
            raise UserError(
                'DÖF sadece Yüksek veya Tolerans Gösterilemez risk seviyesinde açılabilir.'
            )
        severity_map = {'high': 'high', 'intolerable': 'critical'}
        capa = self.env['isg.capa'].create({
            'workplace_id': self.assessment_id.workplace_id.id,
            'site_id': (self.location_id.id or self.assessment_id.site_id.id),
            'source': 'risk_assessment',
            'capa_type': 'corrective',
            'severity': severity_map.get(self.risk_level, 'medium'),
            'open_date': fields.Date.context_today(self),
            'description': 'Risk Değerlendirmesi — %s\nTehlike: %s\nRisk Skoru: %s (%s)' % (
                self.assessment_id.name,
                self.hazard_description,
                self.risk_score,
                dict(self._fields['risk_level'].selection).get(self.risk_level, ''),
            ),
            'risk_line_id': self.id,
        })
        self.capa_id = capa.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.capa',
            'res_id': capa.id,
            'view_mode': 'form',
        }
