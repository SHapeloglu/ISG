# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class IsgTrainingScheduler(models.Model):
    _name = 'isg.training.scheduler'
    _description = 'İSG Eğitim Zamanlayıcı (Cron İşlemleri)'

    name = fields.Char(string='Adı', default='Dönüş Eğitimi Tetikleyicisi', readonly=True)
    last_run = fields.Datetime(string='Son Çalışma Tarihi', readonly=True)

    def action_process_return_training(self):
        """
        Cron job: 6 aydan fazla işten uzak olan çalışanları bulup dönüş eğitimi oluştur.
        RG 33212 Md 7 gereği dönüş eğitimi gerekli.
        """
        six_months_ago = fields.Date.today() - relativedelta(months=6)
        
        # Son çalışma tarihi 6 aydan eski olan çalışanları bul
        employees_need_return_training = self.env['hr.employee'].search([
            ('last_working_date', '!=', False),
            ('last_working_date', '<', six_months_ago),
            ('isg_workplace_id', '!=', False),
        ])
        
        training_type_return = self.env.ref('isg_training.training_type_return')
        created_count = 0
        
        for employee in employees_need_return_training:
            # Dönüş eğitimi kaydı zaten var mı, kontrol et
            existing_training = self.env['isg.training.attendee'].search([
                ('employee_id', '=', employee.id),
                ('record_id.training_type_id', '=', training_type_return.id),
                ('record_id.state', '!=', 'cancelled'),
            ], limit=1)
            
            if existing_training:
                # Zaten var, geç
                continue
            
            # Yeni dönüş eğitimi kaydı oluştur
            training_record = self.env['isg.training.record'].create({
                'name': f'Otomatik Dönüş Eğitimi: {employee.name}',
                'training_type_id': training_type_return.id,
                'training_date': fields.Date.today(),
                'workplace_id': employee.isg_workplace_id.id,
                'duration_hours': 8.0,
                'company_id': employee.company_id.id if employee.company_id else self.env.company.id,
                'attendee_ids': [(0, 0, {
                    'employee_id': employee.id,
                })],
                'state': 'draft',
            })
            created_count += 1
        
        # Son çalışma tarihini güncelle
        self.last_run = fields.Datetime.now()
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Dönüş Eğitimi Tetikleyicisi'),
                'message': _(f'{created_count} çalışan için dönüş eğitimi kaydı oluşturuldu.'),
                'type': 'success',
            }
        }
