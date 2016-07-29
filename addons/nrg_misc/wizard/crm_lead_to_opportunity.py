# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ExtendedCrmLead2opportunityPartner(models.TransientModel):
    """ Inherits crm.partner.binding and select 'Create a new customer' by default when Convert to opportunity. """
    _inherit = 'crm.lead2opportunity.partner'
    
    # Override
    def default_get(self, cr, uid, fields, context=None):
        res = super(ExtendedCrmLead2opportunityPartner, self).default_get(cr, uid, fields, context=context)
        res.update({'action': 'create'})
        return res
