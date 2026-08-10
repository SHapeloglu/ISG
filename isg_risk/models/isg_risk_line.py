from odoo import models, fields, api


class IsgRiskLine(models.Model):
    _name = 'isg.risk.line'
    _description = 'Risk Değerlendirmesi Satırı'
    _order = 'risk_score desc, id asc'

    assessment_id = fields.Many2one(
        'isg.risk.assessment',
        string='Risk Değerlendirmesi',
        required=True,
        ondelete='cascade',
    )
    method = fields.Selection(
        related='assessment_id.method',
        store=True,
    )
    company_id = fields.Many2one(
        related='assessment_id.company_id',
        store=True,
    )

    # --- Tehlike Tanımı ---
    location_id = fields.Many2one(
        'isg.site',
        string='Lokasyon',
    )
    hazard_category = fields.Selection([
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
    ], string='Tehlike Kategorisi', required=True)
    hazard_description = fields.Text(string='Tehlike Tanımı', required=True)
    affected_persons = fields.Char(string='Etkilenen Kişiler / Gruplar')
    existing_controls = fields.Text(string='Mevcut Kontrol Önlemleri')

    # --- L Matrisi Puanlama (5x5) ---
    probability_l = fields.Selection([
        ('1', '1 — Çok Düşük (Neredeyse İmkânsız)'),
        ('2', '2 — Düşük (Küçük İhtimal)'),
        ('3', '3 — Orta (Ara Sıra)'),
        ('4', '4 — Yüksek (Muhtemel)'),
        ('5', '5 — Çok Yüksek (Kaçınılmaz)'),
    ], string='Olasılık (L)')
    severity_l = fields.Selection([
        ('1', '1 — Önemsiz (İlk Yardım)'),
        ('2', '2 — Hafif (Kayıp İş Günü Yok)'),
        ('3', '3 — Orta (Kayıp İş Günü)'),
        ('4', '4 — Ağır (Sürekli İş Göremezlik)'),
        ('5', '5 — Çok Ağır (Ölüm / Toplu Kaza)'),
    ], string='Şiddet (L)')

    # --- Fine-Kinney Puanlama ---
    probability_fk = fields.Selection([
        ('0.2', '0.2 — Çok Uzak İhtimal'),
        ('0.5', '0.5 — Uzak İhtimal'),
        ('1', '1 — Düşük İhtimal'),
        ('3', '3 — Olağandışı Ama Mümkün'),
        ('6', '6 — Olası'),
        ('10', '10 — Çok Olası'),
    ], string='Olasılık (FK)')
    frequency_fk = fields.Selection([
        ('0.5', '0.5 — Çok Nadir (Yılda 1)'),
        ('1', '1 — Nadir (Yılda Birkaç)'),
        ('2', '2 — Ara Sıra (Ayda 1)'),
        ('3', '3 — Düzenli (Haftada 1)'),
        ('6', '6 — Sık (Günlük)'),
        ('10', '10 — Sürekli'),
    ], string='Frekans (FK)')
    severity_fk = fields.Selection([
        ('1', '1 — Küçük Yaralanma'),
        ('3', '3 — Önemli Yaralanma'),
        ('7', '7 — Ağır Yaralanma'),
        ('15', '15 — Tek Ölüm'),
        ('40', '40 — Birden Fazla Ölüm'),
        ('100', '100 — Felaket'),
    ], string='Şiddet (FK)')

    # --- Risk Skoru (compute) ---
    risk_score = fields.Float(
        string='Risk Skoru',
        compute='_compute_risk_score',
        store=True,
    )
    risk_level = fields.Selection([
        ('acceptable', 'Kabul Edilebilir'),
        ('low', 'Düşük Risk'),
        ('medium', 'Orta Risk'),
        ('high', 'Yüksek Risk'),
        ('intolerable', 'Tolerans Gösterilemez'),
    ], string='Risk Seviyesi', compute='_compute_risk_score', store=True)

    # --- Kontrol Önlemleri ---
    control_hierarchy = fields.Selection([
        ('elimination', '1 — Ortadan Kaldırma'),
        ('substitution', '2 — İkame'),
        ('engineering', '3 — Mühendislik Kontrolü'),
        ('administrative', '4 — İdari Kontrol'),
        ('ppe', '5 — KKD'),
    ], string='Kontrol Hiyerarşisi')
    additional_controls = fields.Text(string='Planlanan Ek Kontroller')
    responsible_id = fields.Many2one('hr.employee', string='Sorumlu')
    deadline = fields.Date(string='Termin')

    # --- Kalıntı Risk ---
    residual_probability_l = fields.Selection([
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ], string='Kalıntı Olasılık (L)')
    residual_severity_l = fields.Selection([
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ], string='Kalıntı Şiddet (L)')
    residual_probability_fk = fields.Selection([
        ('0.2', '0.2'), ('0.5', '0.5'), ('1', '1'),
        ('3', '3'), ('6', '6'), ('10', '10'),
    ], string='Kalıntı Olasılık (FK)')
    residual_frequency_fk = fields.Selection([
        ('0.5', '0.5'), ('1', '1'), ('2', '2'),
        ('3', '3'), ('6', '6'), ('10', '10'),
    ], string='Kalıntı Frekans (FK)')
    residual_severity_fk = fields.Selection([
        ('1', '1'), ('3', '3'), ('7', '7'),
        ('15', '15'), ('40', '40'), ('100', '100'),
    ], string='Kalıntı Şiddet (FK)')

    residual_score = fields.Float(
        string='Kalıntı Risk Skoru',
        compute='_compute_residual_score',
        store=True,
    )
    residual_level = fields.Selection([
        ('acceptable', 'Kabul Edilebilir'),
        ('low', 'Düşük Risk'),
        ('medium', 'Orta Risk'),
        ('high', 'Yüksek Risk'),
        ('intolerable', 'Tolerans Gösterilemez'),
    ], string='Kalıntı Risk Seviyesi', compute='_compute_residual_score', store=True)

    capa_id = fields.Many2one(
        'isg.capa',
        string='İlgili DÖF',
        readonly=True,
    )

    # -------------------------------------------------------------------------
    # Yardımcı metodlar
    # -------------------------------------------------------------------------

    def _level_from_score_l(self, score):
        # L Matrisi 5x5: max=25
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

    def _level_from_score_fk(self, score):
        # Fine-Kinney standart bantları
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

    # -------------------------------------------------------------------------
    # Compute
    # -------------------------------------------------------------------------

    @api.depends(
        'method',
        'probability_l', 'severity_l',
        'probability_fk', 'frequency_fk', 'severity_fk',
    )
    def _compute_risk_score(self):
        for rec in self:
            if rec.method == 'l_matrix':
                p = int(rec.probability_l or 0)
                s = int(rec.severity_l or 0)
                score = p * s
                rec.risk_score = score
                rec.risk_level = self._level_from_score_l(score) if score else False
            else:
                p = float(rec.probability_fk or 0)
                f = float(rec.frequency_fk or 0)
                s = float(rec.severity_fk or 0)
                score = p * f * s
                rec.risk_score = score
                rec.risk_level = self._level_from_score_fk(score) if score else False

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
                rec.residual_level = self._level_from_score_l(score) if score else False
            else:
                p = float(rec.residual_probability_fk or 0)
                f = float(rec.residual_frequency_fk or 0)
                s = float(rec.residual_severity_fk or 0)
                score = p * f * s
                rec.residual_score = score
                rec.residual_level = self._level_from_score_fk(score) if score else False

    # -------------------------------------------------------------------------
    # Yüksek risk → otomatik DÖF
    # -------------------------------------------------------------------------

    def action_create_capa(self):
        self.ensure_one()
        if self.capa_id:
            raise UserError('Bu satır için zaten bir DÖF kaydı mevcut: %s' % self.capa_id.name)
        if self.risk_level not in ('high', 'intolerable'):
            raise UserError('Otomatik DÖF sadece Yüksek veya Tolerans Gösterilemez risk seviyesinde açılabilir.')
        capa = self.env['isg.capa'].create({
            'company_id': self.assessment_id.company_id.id,
            'workplace_id': self.assessment_id.workplace_id.id,
            'source': 'risk',
            'risk_assessment_id': self.assessment_id.id,
            'description': 'Risk Değerlendirmesi — %s\nTehlike: %s\nRisk Skoru: %s (%s)' % (
                self.assessment_id.name,
                self.hazard_description,
                self.risk_score,
                dict(self._fields['risk_level'].selection).get(self.risk_level, ''),
            ),
            'responsible_id': self.responsible_id.user_id.id if self.responsible_id and self.responsible_id.user_id else False,
            'deadline': self.deadline,
        })
        self.capa_id = capa.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'isg.capa',
            'res_id': capa.id,
            'view_mode': 'form',
        }
