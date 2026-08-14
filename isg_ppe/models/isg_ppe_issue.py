# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class IsgPpeIssue(models.Model):
    _name = 'isg.ppe.issue'
    _description = 'KKD Zimmet Kaydı'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'issue_date desc, id desc'

    name = fields.Char(
        string='Zimmet No', required=True, copy=False,
        readonly=True, default=lambda self: 'Yeni',
    )
    company_id = fields.Many2one(
        'res.company', string='Şirket', required=True,
        default=lambda self: self.env.company,
    )
    workplace_id = fields.Many2one(
        'isg.workplace', string='İSG İşyeri', required=True,
    )
    employee_id = fields.Many2one(
        'hr.employee', string='Çalışan', required=True, tracking=True,
    )

    # Çalışanın beden ölçüleri (isg_hr'dan otomatik)
    employee_clothing_size = fields.Selection(
        related='employee_id.ppe_clothing_size',
        string='Kıyafet Bedeni', readonly=True,
    )
    employee_shoe_size = fields.Char(
        related='employee_id.ppe_shoe_size',
        string='Ayakkabı Numarası', readonly=True,
    )
    employee_glove_size = fields.Selection(
        related='employee_id.ppe_glove_size',
        string='Eldiven Bedeni', readonly=True,
    )

    ppe_type_id = fields.Many2one(
        'isg.ppe.type', string='KKD Türü', required=True, tracking=True,
    )
    size = fields.Char(string='Beden / Numara')
    brand = fields.Char(string='Marka / Model')
    quantity = fields.Integer(string='Adet', default=1)
    issue_date = fields.Date(
        string='Zimmet Tarihi', required=True,
        default=fields.Date.context_today, tracking=True,
    )
    expiry_date = fields.Date(
        string='Son Kullanım / Yenileme Tarihi',
        compute='_compute_expiry_date', store=True,
    )
    return_date = fields.Date(string='İade Tarihi', tracking=True)
    document_id = fields.Many2one('isg.document', string='Zimmet Belgesi')
    notes = fields.Text(string='Notlar')

    state = fields.Selection(
        [
            ('issued', 'Zimmetli'),
            ('returned', 'İade Edildi'),
            ('expired', 'Süresi Doldu'),
            ('lost', 'Kayıp / Hasarlı'),
        ],
        string='Durum', default='issued', tracking=True, copy=False,
    )

    @api.depends('issue_date', 'ppe_type_id.lifespan_months')
    def _compute_expiry_date(self):
        for rec in self:
            if rec.issue_date and rec.ppe_type_id.lifespan_months:
                rec.expiry_date = rec.issue_date + relativedelta(
                    months=rec.ppe_type_id.lifespan_months
                )
            else:
                rec.expiry_date = False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Yeni') == 'Yeni':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'isg.ppe.issue'
                ) or 'Yeni'
        return super().create(vals_list)

    def action_return(self):
        for rec in self:
            if rec.state != 'issued':
                raise UserError('Sadece zimmetli KKD iade alınabilir.')
            rec.write({
                'state': 'returned',
                'return_date': fields.Date.context_today(self),
            })

    def action_lost(self):
        self.write({'state': 'lost'})

    def action_reissue(self):
        self.write({'state': 'issued', 'return_date': False})
