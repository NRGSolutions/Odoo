# -*- config: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError

class ExtendedSaleOrder(models.Model):
    """ Inherits sale.order and adds Demo state """
    _inherit = 'sale.order'
    
    nrg_demo_is_demo = fields.Boolean('With Demo', default=False, readonly=True,
                                      states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                      help='Sale order for demo or not.')
    
    # Override
    @api.multi
    def _prepare_invoice(self):
        """ COMMENT """
        invoice_vals = super(ExtendedSaleOrder, self)._prepare_invoice()

        target_journal_id = None
        if self.nrg_demo_is_demo:
            demo_journal_id = self.env['ir.values'].get_default('account.config.settings', 'nrg_demo_journal_id')
            if not demo_journal_id:
                raise UserError(_('Please define an journal ID for demo.'))                
            target_journal_id = demo_journal_id
        else:
            normal_journal_id = self.env['ir.values'].get_default('account.config.settings', 'nrg_demo_normal_journal_id')
            if normal_journal_id:
                target_journal_id = normal_journal_id
            else:
                target_journal_id = invoice_vals['journal_id']
        
        invoice_vals['journal_id'] = target_journal_id
        return invoice_vals
