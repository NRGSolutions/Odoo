# -*- config: utf-8 -*-
from openerp import models, fields, api, _

class NrgAccountingPaytype(models.Model):
    _name = 'nrg.accounting.paytype'
    
    name = fields.Char('Name', required=True)
    is_require_fund = fields.Boolean('Require Fund?', default=False)
    

class NrgAccountingPaytypeFund(models.Model):
    _name = 'nrg.accounting.paytype.fund'
    
    name = fields.Char('Name', required=True)
