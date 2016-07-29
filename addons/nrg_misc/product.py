# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedProductTemplate(models.Model):
    """ Inherits product.template and make "Track Serial" default. """
    _inherit = 'product.template'
    
    _defaults = {
        'tracking': 'serial',
    }
