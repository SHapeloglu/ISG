from odoo import models, fields, api

ISG_CATEGORY_NAME = 'İSG Platform'


class ResUsers(models.Model):
    _inherit = 'res.users'

    # Kullanıcının erişebileceği İSG işyerleri
    isg_workplace_ids = fields.Many2many(
        'isg.workplace',
        'res_users_isg_workplace_rel',
        'user_id',
        'workplace_id',
        string='Erişim İzni Verilen İşyerleri',
        help='Boş bırakılırsa şirket bazlı erişim geçerlidir.',
    )

    # İSG gruplarını filtreli göstermek için computed field
    isg_group_ids = fields.Many2many(
        'res.groups',
        string='İSG Grupları',
        compute='_compute_isg_group_ids',
        inverse='_set_isg_group_ids',
    )

    @api.depends('groups_id')
    def _compute_isg_group_ids(self):
        for user in self:
            user.isg_group_ids = user.groups_id.filtered(
                lambda g: g.category_id.name == ISG_CATEGORY_NAME
            )

    def _set_isg_group_ids(self):
        for user in self:
            # Mevcut İSG gruplarını kaldır
            isg_groups = self.env['res.groups'].search([
                ('category_id.name', '=', ISG_CATEGORY_NAME)
            ])
            user.groups_id = (
                user.groups_id - isg_groups + user.isg_group_ids
            )
