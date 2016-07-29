# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedTask(models.Model):
    """ Inherits project.task and adds an reference to sale.order. """
    _inherit = 'project.task'
    
    nrg_asp_sale_order = fields.Many2one('sale.order', 'Parent Sale Order',
                                         help='Related sale order.')
    nrg_asp_incharge = fields.Selection([
                            ('admin', 'Office Manager'),    # Corresponding to the variable name in sale.order.
                            ('technician', 'Technician'),   # Corresponding to the variable name in sale.order.
                       ], 
                       'In Charge', 
                       help='Settings for tasks in a template project. Select one of roles which this task should be assigned to.')
    nrg_asp_deadline_days = fields.Integer('Default Deadline (days)', 
                                           help='Settings for tasks in a template project. A deadine of this task is set specified days after a sale order is created.')
    nrg_asp_is_in_template = fields.Boolean('TEMP', compute='_compute_is_in_template')
    
    nrg_asp_ref_so_warehouse = fields.Many2one('Warehouse', related="nrg_asp_sale_order.warehouse_id")


    @api.one
    @api.depends('project_id')
    def _compute_is_in_template(self):
        self.nrg_asp_is_in_template = self.project_id.nrg_asp_is_template
    
    # Override
    def onchange_project(self, cr, uid, id, project_id, context=None):
        ret = super(ExtendedTask, self).onchange_project(cr, uid, id, project_id, context)
        project = self.pool.get('project.project').browse(cr, uid, project_id, context=context)
        ret['value']['nrg_asp_is_in_template'] = project.nrg_asp_is_template
        return ret
    
    @api.onchange('project_id')
    def _onchange_project_id(self):
        self.nrg_asp_is_in_template = self.project_id.nrg_asp_is_template



class ExtendedProject(models.Model):
    """ Inherits project.project and adds template settings. """
    _inherit = 'project.project'
    
    nrg_asp_so_warehouse = fields.Many2one('stock.warehouse', 'Warehouse')
    nrg_asp_is_template = fields.Boolean('Is Template', 
                                         default=False, 
                                         help='Template projects can be specified in a sale order form for creating an after-sales service project.')
    