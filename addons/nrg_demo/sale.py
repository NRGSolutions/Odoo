# -*- config: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError

# Two lines below added by Sejin Park on 08/01/2016
# Doesn't seem necessary
# from calendar import calendar.event
# from datetime import timedelta

class ExtendedSaleOrder(models.Model):
    """ Inherits sale.order and adds Demo state """
    _inherit = 'sale.order'
    
    nrg_demo_is_demo = fields.Boolean('With Demo', default=False, readonly=True,
                                      states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                      help='Sale order for demo or not.')

    # Two lines below added by Sejin Park on 08/02/2016
    nrg_demo_template_calendar = fields.Many2one('calendar.event', 'Schedule Demo Checkup', readonly=True, 
                                              states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
                                               # domain="[('nrg_demo_cal_is_template', '=', 1)]",
                                               help='Select if sale is with demo')
    # _PREFIX_EVENT_NAME = 'Demo Checkup For '
    
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

    # Function below added by Sejin Park on 08/02/2016
    # Not working
    """
    @api.multi
    def action_confirm(self):
        super(ExtendedSaleOrder, self).action_confirm()

        for sale in self:
            if sale.nrg_demo_is_demo:
                template_calendar = sale.nrg_demo_template_calendar
                if not template_calendar:
                    raise UserError(_('Please specify a template project for demo check-up.'))

            self.env['calendar.event'].write({'partner_ids': sale.partner_id.id})
            """




