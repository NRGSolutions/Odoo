# -*- config: utf-8 -*-
from openerp import fields, models, api, _

class PaygManagement(models.Model):
    """ """
    _name = "nrg.payg"
    _description=""
#     _order = ''
    
    nrg_payg_is_active = fields.Boolean('Active', default=True)
    
    nrg_payg_name = fields.Char('Name', required=True)
    nrg_payg_date = fields.Datetime('Generated Date')
    nrg_payg_client = fields.Char('Client')
    nrg_payg_payment = fields.Char('Payment')
    nrg_payg_product = fields.Many2one('stock.quant', 'Assigned Product')

    nrg_payg_initial_code = fields.Char('Install Code', required=True)
    nrg_payg_unlock_code = fields.Char('Unlock Code')
    nrg_payg_credit_codes = fields.One2many(
                                'nrg.payg.id',
                                'nrg_payg_id_parent', 
                                'Credit Codes',
                            )


class PaygId(models.Model):
    _name = "nrg.payg.id"
    
    nrg_payg_id_parent = fields.Many2one('nrg.payg', 'Parent')
    nrg_payg_id_index = fields.Integer('Index', readonly=True)
    nrg_payg_id_id = fields.Char('Credit Code', required=True)
    nrg_payg_id_paid_date = fields.Datetime('Paid Date')
