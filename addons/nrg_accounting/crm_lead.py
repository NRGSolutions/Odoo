# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedLead(models.Model):
    """ Inherits crm.lead and adds automatic settings of default receivable and payable accounts. """
    _inherit = 'crm.lead'
    
    # Override
    def _lead_create_contact(self, cr, uid, lead, name, is_company, parent_id=False, context=None):
        partner_id = super(ExtendedLead, self)._lead_create_contact(cr, uid, lead, name, is_company, parent_id, context)
        partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
        
        # Set default receivable and payable accounts.
        acct_recv_id = self.pool.get('ir.values').get_default(cr, uid, 'account.config.settings', 'nrg_accounting_default_account_receivable')
        partner.property_account_receivable_id = self.pool.get('account.account').browse(cr, uid, acct_recv_id, context=context)
        acct_pay_id = self.pool.get('ir.values').get_default(cr, uid, 'account.config.settings', 'nrg_accounting_default_account_payable')
        partner.property_account_payable_id = self.pool.get('account.account').browse(cr, uid, acct_pay_id, context=context)
        
        return partner_id
