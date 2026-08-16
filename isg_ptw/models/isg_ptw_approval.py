# -*- coding: utf-8 -*-
from odoo import api, fields, models

class IsgPtwApproval(models.Model):
    _name = 'isg.ptw.approval'
    _description = 'İş İzni Onay Adımı'
    _order = 'sequence, id'

    sequence = fields.Integer(string='Sıra', default=10)
    
    ptw_id = fields.Many2one(
        'isg.ptw',
        string='İş İzni',
        required=True,
        ondelete='cascade',
    )
    
    # Onaylayan rol
    approval_role = fields.Selection(
        [
            ('supervisor', 'Bölüm Amiri'),
            ('expert', 'İSG Uzmanı'),
            ('physician', 'İşyeri Hekimi'),
            ('manager', 'İSG Yöneticisi'),
        ],
        string='Onaylayan Rol',
        required=True,
    )
    
    # Onaylayan kişi
    approver_id = fields.Many2one(
        'res.users',
        string='Onaylayan',
    )
    
    # Durum
    state = fields.Selection(
        [
            ('pending', 'Bekleyen'),
            ('approved', 'Onaylandı'),
            ('rejected', 'Reddedildi'),
            ('skipped', 'Geçildi'),
        ],
        string='Durum',
        default='pending',
    )
    
    # Onay tarihi
    approval_date = fields.Datetime(
        string='Onay Tarihi',
    )
    
    # Onay notları
    approval_notes = fields.Text(
        string='Onay Notları',
    )
    
    def action_approve(self):
        """Bu onay adımını onayla"""
        for record in self:
            record.write({
                'state': 'approved',
                'approval_date': fields.Datetime.now(),
                'approver_id': self.env.user.id,
            })
            # Sonraki adıma git
            next_approval = record.ptw_id.approval_ids.filtered(
                lambda a: a.sequence > record.sequence and a.state == 'pending'
            ).sorted('sequence')
            if not next_approval:
                # Tüm onaylar yapıldı
                record.ptw_id.write({'state': 'approved'})
    
    def action_reject(self):
        """Bu onay adımını reddet"""
        for record in self:
            record.write({
                'state': 'rejected',
                'approval_date': fields.Datetime.now(),
                'approver_id': self.env.user.id,
            })
            # İzni reddet
            record.ptw_id.write({'state': 'rejected'})
