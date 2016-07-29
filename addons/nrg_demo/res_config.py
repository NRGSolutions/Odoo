# -*- config: utf-8 -*-

# from openerp import SUPERUSER_ID
from openerp import models, fields, api

class ExtendedAccountConfigSettings(models.TransientModel):
    """ Inherits account.config.settings and adds Journal configuration for demo. """
    _inherit = 'account.config.settings'

    nrg_demo_normal_journal_id = fields.Many2one('account.journal', string='Journal for Sale')
    nrg_demo_journal_id = fields.Many2one('account.journal', string='Journal for Demo')
    
    @api.one
    def set_journal_defaults(self):
#         self.ensure_one()

#         if not self.env.user._is_admin():
#             raise AccessError(_("Only admiinstrators can change the settings."))
#         self.env['ir.values'].sudo().set_default('sale.config.settings', 'nrg_demo_journal_id', self.nrg_demo_journal_id.id)
        self.env['ir.values'].set_default('account.config.settings', 'nrg_demo_normal_journal_id', self.nrg_demo_normal_journal_id.id)
        self.env['ir.values'].set_default('account.config.settings', 'nrg_demo_journal_id', self.nrg_demo_journal_id.id)
