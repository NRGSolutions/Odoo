# -*- config: utf-8 -*-
from openerp import models, fields, api, _

class ExtendedProduct(models.Model):
    """ Inherits product.template and adds PAYG ID management. """
    _inherit = 'product.template'
    
    nrg_payg_is_payg = fields.Boolean('Is Pay-As-You-Go', default=False)
