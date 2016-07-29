# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedAccountConfigSettings(models.TransientModel):
    """ Inherits account.config.settings and adds ... """
    _inherit = 'account.config.settings'
    
    nrg_accounting_default_account_receivable= fields.Many2one('account.account', 
                                                               string='Default Receivable Account', 
                                                            default=lambda self: self.env['ir.model.data'].xmlid_to_res_id('nrg_accounting.nrg_accounting_account_default_receivable'))
    nrg_accounting_default_account_payable = fields.Many2one('account.account', 
                                                             string='Default Payable Account', 
                                                             default=lambda self: self.env['ir.model.data'].xmlid_to_res_id('nrg_accounting.nrg_accounting_account_default_payable'))
    
    @api.one
    def set_account_defaults(self):
        self.env['ir.values'].set_default('account.config.settings', 'nrg_accounting_default_account_receivable', self.nrg_accounting_default_account_receivable.id)
        self.env['ir.values'].set_default('account.config.settings', 'nrg_accounting_default_account_payable', self.nrg_accounting_default_account_payable.id)
