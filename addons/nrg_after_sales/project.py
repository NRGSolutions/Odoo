# -*- config: utf-8 -*-
from openerp import models, fields, api
from datetime import date, datetime

import logging
_logger = logging.getLogger(__name__)

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
   
    # ------------------------------------------------
    # Lines edited by Florian on 02/08/2016
    # ------------------------------------------------

    nrg_asp_delay = fields.Date('Ending_Date')
    nrg_asp_is_late = fields.Boolean('Late', default= False) 
    nrg_asp_is_reactive = fields.Boolean('After Sales Reactive', default=False)
    nrg_asp_problem_description = fields.Selection([
					('option1', 'option1'), ('option2','option2'),], 'Description of the problem')
    nrg_asp_solution_description = fields.Selection([('option1', 'option1'), ('option2','option2'),],'Description of the solution') 
    nrg_asp_problem_identification = fields.Selection([('option1', 'option1'), ('option2','option2'),],'How the problem was identified') 
    nrg_asp_notes = fields.Text('Notes')


    def write(self, cr, uid, ids, vals, context=None):

	# To get the stage id of the stage "done"
	done_stage_id = self.pool.get('project.task.type').search(cr, uid, [('name','=','Done')], order='sequence', context=context)[0]
	todo_stage_id = self.pool.get('project.task.type').search(cr, uid, [('name','=','Done')], order='sequence', context=context)[0]
	doing_stage_id = self.pool.get('project.task.type').search(cr, uid, [('name','=','Done')], order='sequence', context=context)[0]

	#Put the ending_date if the task is set to "done" stage
	if vals and 'stage_id' in vals and vals.get('stage_id') == done_stage_id:				
            vals['nrg_asp_delay'] = fields.Date.today()
	else:
            vals['nrg_asp_delay'] = None

	result=super(ExtendedTask, self).write( cr, uid, ids, vals, context=context )
	return result
		
    # ------------------------------------------------
    # Other functions
    # ------------------------------------------------
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
    
