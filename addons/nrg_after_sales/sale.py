# -*- config: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import UserError

from datetime import date
from dateutil.relativedelta import relativedelta

class ExtendedSaleOrder(models.Model):
    """ Inherits sale.order and adds project creation. """
    _inherit = 'sale.order'

    nrg_asp_create_project = fields.Boolean('Create After-Sales Project', default=True, readonly=True,
                                            states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                            help='Create a project and tasks for after-sales service automatically or not.')
    nrg_asp_template_project = fields.Many2one('project.project', 'Template Project', readonly=True, 
                                               states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
                                               domain="[('nrg_asp_is_template', '=', 1)]",
                                               help='Specify a template project which an after-sales project are created based on.')
    nrg_asp_admin = fields.Many2one('res.users', 'Office Manager', readonly=True,
                                    states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
                                    help='Specify a user as a local administrator role.')    # Don't change the variable name.
    # Line edited by Sejin, 07/29/2016
    nrg_asp_technician = fields.Many2one('res.users', 'Technician', readonly=True,
                                         states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
                                         help='Specify a user as a local technician role.', required=True)  # Don't change the variable name.

    _PREFIX_PROJECT_NAME = 'After Sales For '
    
    # Override
    @api.multi
    def action_confirm(self):
        super(ExtendedSaleOrder, self).action_confirm()

        for sale in self:
            if sale.nrg_asp_create_project:
                template_project = sale.nrg_asp_template_project
                if not template_project:
                    raise UserError(_('Please specify a template project for after-sales service.'))
                
                # Find existing projects for the customer.
                customer_projects = self.env['project.project'].search([('partner_id', '=', sale.partner_id.id)])
                if customer_projects:
                    # If a project for the customer already exists.
                    customer_project = customer_projects[0]
                    for task in self.env['project.task'].browse(template_project.task_ids.ids):
                        new_task_params = self._set_task_parameters(sale, task)
                        new_task_params['project_id'] = customer_project.id
                        new_task = task.copy(new_task_params)
                        customer_project.task_ids += new_task
                else:
                    # If a project for the customer has yet to exist.
                    project_new = template_project.copy({
                        'name': sale._PREFIX_PROJECT_NAME + sale.partner_id.name,
                        'partner_id': sale.partner_id.id,
                        'user_id': self.user_id.id,         # Project Manager
                        'nrg_asp_is_template': False,
                        'nrg_asp_so_warehouse': sale.warehouse_id.id,
#                         'analytic_account_id': '',          # Contract/Analytic (account.analytic.account)
                    })
        
                    for task in self.env['project.task'].browse(project_new.task_ids.ids):
                        task.write(self._set_task_parameters(sale, task))


    # Create task settings.
    def _set_task_parameters(self, src_sale_order, src_stock_task):
        return {
            'name': src_stock_task.name + ' (' + src_sale_order.name + ')',
            'partner_id': src_sale_order.partner_id.id,
            'user_id': src_stock_task.nrg_asp_incharge and src_sale_order['nrg_asp_' + src_stock_task.nrg_asp_incharge].id or False,
            'stage_id': src_stock_task.stage_id.id,
            'nrg_asp_sale_order': src_sale_order.id,
            'date_deadline': src_stock_task.nrg_asp_deadline_days and self._calc_deadline_date_str(src_sale_order.create_date, src_stock_task.nrg_asp_deadline_days) or False,
#             'planned_hours': '',
#             'remaining_hours': '',
#             'procurement_id': '',
#             'description': '',
#             'company_id': '',
        }

    # Calculate deadline of task.            
    def _calc_deadline_date_str(self, from_datetime_str, delta_days):
        return fields.Date.to_string(fields.Datetime.from_string(from_datetime_str).date() + relativedelta(days=delta_days))
