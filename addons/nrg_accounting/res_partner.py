# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedResPartner(models.Model):
    """ Inherits res.partner and adds ... """
#     _name = 'res.partner'
    _inherit = 'res.partner'

# #     def _get_default_receivable_account(self, cr, uid, context=None):
    @api.model
    def _default_property_account_receivable(self):
        id = self.env['ir.values'].get_default('account.config.settings', 'nrg_accounting_default_account_receivable')
        t = self.env['account.account'].browse(id)
#         self.property_account_receivable_id = self.env['account.account'].browse(id)
        return self.env['account.account'].browse(id)

# #     def _get_default_payable_account(self, cr, uid, context=None):
    @api.model
    def _default_property_account_payable(self):
        id = self.env['ir.values'].get_default('account.config.settings', 'nrg_accounting_default_account_payable')
        t = self.env['account.account'].browse(id)
#         self.property_account_payable_id = self.env['account.account'].browse(id)
        return self.env['account.account'].browse(id)
#     

    @api.model
    def _default_phonea(self):
        return '99999'

#     _defaults = {
#         'property_account_receivable_id': lambda self: self.env['account.account'].browse(self.env['ir.values'].get_default('account.config.settings', 'nrg_accounting_default_account_receivable')),
#         'property_account_payable_id': lambda self: self.env['account.account'].browse(self.env['ir.values'].get_default('account.config.settings', 'nrg_accounting_default_account_payable')),
#         'property_account_receivable_id': _default_property_account_receivable,
#         'property_account_payable_id': _default_property_account_payable,
#         'phone': _default_phonea
#     }

#     property_account_receivable_id = fields.Many2one('account.account', company_dependent=True,
#         string="Account Receivable", oldname="property_account_receivable",
#         domain="[('internal_type', '=', 'receivable'), ('deprecated', '=', False)]",
#         help="This account will be used instead of the default one as the receivable account for the current partner",
#         required=True, default=_default_property_account_receivable)
#     property_account_payable_id = fields.Many2one('account.account', company_dependent=True,
#         string="Account Payable", oldname="property_account_payable",
#         domain="[('internal_type', '=', 'payable'), ('deprecated', '=', False)]",
#         help="This account will be used instead of the default one as the payable account for the current partner",
#         required=True, default=_default_property_account_payable)

