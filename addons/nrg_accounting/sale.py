# -*- config: utf-8 -*-
from openerp import models, fields, api, _

class ExtendedSaleOrder(models.Model):
    """ Inherits sale.order and adds payment type. """
    _inherit = 'sale.order'
    
    nrg_accounting_paytype = fields.Many2one('nrg.accounting.paytype', 'Payment Type', required=True)
    nrg_accounting_paytype_fund = fields.Many2one('nrg.accounting.paytype.fund', 'Fund')
    nrg_accounting_ref_paytype_isfund = fields.Boolean('Require Fund', related='nrg_accounting_paytype.is_require_fund')
