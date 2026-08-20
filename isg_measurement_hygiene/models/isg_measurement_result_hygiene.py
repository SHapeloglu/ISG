# -*- coding: utf-8 -*-
from odoo import api, fields, models


class IsgMeasurementResultHygiene(models.Model):
    _inherit = 'isg.measurement.result'
    _description = 'Ölçüm Sonucu — Hijyen Parametreleri Uzantısı'

    # === PARAMETER TİPİ ===
    measurement_type = fields.Selection(
        [
            ('noise', 'Gürültü'),
            ('dust', 'Toz'),
            ('vibration', 'Titreşim'),
            ('illumination', 'Aydınlatma'),
            ('thermal', 'Isıl Konfor'),
        ],
        string='Hijyen Parametresi',
        help='Hangi türde ölçüm bu kaydı temsil ediyor',
    )

    # === GÜRÜLTÜ (NOISE) — LAeq, LCeq, Lpeak ===
    laeq_value = fields.Float(
        string='LAeq (dB)',
        help='A-ağırlıklı eşdeğer ses basınç seviyesi — 8 saat veya vardiya süresi',
    )
    lceq_value = fields.Float(
        string='LCeq (dB)',
        help='C-ağırlıklı eşdeğer ses basınç seviyesi',
    )
    lpeak_value = fields.Float(
        string='Lpeak (dB)',
        help='Tepe ses basınç seviyesi — anlık maksimum',
    )
    lpeak_reference = fields.Float(
        string='Lpeak Referans Limit (dB)',
        default=140,
        help='Tepe ses basınç seviyesi mevzuat limiti — TÜRKIYE ÇSGB: 140 dB',
    )

    # İleride eklenecek: toz, titreşim, aydınlatma, ısıl konfor alanları
    # (F3-002 devam sürümlerinde)

    @api.onchange('measurement_type')
    def _onchange_measurement_type(self):
        """Parametre türü değişince unit ve limit önerileri güncelle"""
        if self.measurement_type == 'noise':
            self.unit = 'dB'
        elif self.measurement_type == 'dust':
            self.unit = 'mg/m³'
        elif self.measurement_type == 'vibration':
            self.unit = 'm/s²'
        elif self.measurement_type == 'illumination':
            self.unit = 'Lux'
        elif self.measurement_type == 'thermal':
            self.unit = '°C' or 'PMV'

    def action_create_capa(self):
        """Limit aşımı durumunda otomatik DÖF oluştur — gürültüye özel açıklama"""
        self.ensure_one()
        if self.compliance_status != 'exceeding':
            return False

        description = f'Parameter: {self.get_measurement_type_display()}\n'
        
        if self.measurement_type == 'noise':
            description += f'LAeq: {self.laeq_value} dB\n'
            description += f'Limit: {self.limit_twa_snapshot} dB\n'
            description += f'Aşım: {self.exceeding_percentage:.1f}%'
        else:
            description += f'Sonuç: {self.raw_value} {self.unit}\n'
            description += f'Limit: {self.limit_twa_snapshot} {self.unit}\n'
            description += f'Aşım: {self.exceeding_percentage:.1f}%'

        capa_vals = {
            'name': f'Hijyen Ölçüm Aşımı: {self.sample_id.name} ({self.measurement_date})',
            'source': 'measurement',
            'description': description,
            'workplace_id': self.workplace_id.id,
            'severity': 'high' if self.exceeding_percentage > 150 else 'medium',
        }
        capa = self.env['isg.capa'].create(capa_vals)
        self.write({'capa_id': capa.id})
        return capa
