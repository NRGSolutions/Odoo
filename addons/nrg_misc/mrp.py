# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedMrpBom(models.Model):
    """ Inherits mrp.bom and ... """
    _inherit = 'mrp.bom'
    
    _defaults = {
        'type': lambda *a: 'phantom',
    }
