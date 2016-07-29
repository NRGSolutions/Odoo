# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedStockQuant(models.Model):
    """ Inherits stock.quant. """
    _inherit = 'stock.quant'

    nrg_misc_ref_proc_group_name = fields.Char('Procurement Group', 
                                               compute='_compute_related_proc_group_name', 
                                               select=True, store=True)
    
    @api.one
    @api.depends('history_ids')
    def _compute_related_proc_group_name(self):
        soname = None
        latest_move = max(self.history_ids, key=(lambda x: x['date']))
        soname = latest_move and latest_move.group_id and latest_move.group_id.name
        self.nrg_misc_ref_proc_group_name = soname or 'Undefined'
