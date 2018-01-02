from odoo import fields, models, api

class TestPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
                                   string="Attended Sessions", readonly=True)

    # @api.model
    # def search(self, args, offset=0, limit=None, order=None, count=False):
    #     user = self.env['res.users'].browse(self._uid)
    #     args.append(('user_id','=',self._uid))
    #     res = super(TestPartner, self).search(args=args, offset=offset, limit=limit, order=order, count=count)
    #     return res

