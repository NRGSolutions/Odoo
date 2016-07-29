# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedResUsers(models.Model):
    """ Inherits res.users and adds ACLs """
    _inherit = 'res.users'
    nrg_acl_warehouse_ids = fields.Many2many('stock.warehouse', string='Warehouses')
    nrg_acl_location_ids = fields.Many2many('stock.location', string='Locations')
    nrg_acl_village_ids = fields.Many2many('nrg.village', string='Villages')
