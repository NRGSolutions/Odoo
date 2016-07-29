# -*- config: utf-8 -*-

from openerp import models, fields, api

class ExtendedProjectProject(models.Model):
    """ Inherits project.project """
    _inherit = 'project.project'

#     nrg_misc_task_assigned_users = fields.Many2many('res.users', string="Assigned Users", compute='_compute_assigned_users')
# #     nrg_misc_is_include_my_task = fields.Boolean("Assigned Users", compute='_compute_assigned_users', store=True)
# 
#     @api.one
#     @api.depends('tasks')
#     def _compute_assigned_users(self):
#         user_ids = []
# #         is_my_task = False
#         for task in self.tasks:
#             if task.user_id:
#                 user_ids.append(task.user_id.id)
# #                 if self.user.id == task.user_id.id:
# #                     is_my_task = False
#         self.nrg_misc_task_assigned_users = self.env['res.users'].browse(user_ids)
# #         self.nrg_misc_is_include_my_task = is_my_task
