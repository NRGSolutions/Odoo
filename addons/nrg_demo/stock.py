# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedStockQuant(models.Model):
    """ Inherits stock.quant and adds demo status. """
    _inherit = 'stock.quant'
    
    nrg_demo_is_demo = fields.Boolean('Is Demo', default=False)
    nrg_demo_at_customer = fields.Boolean('At Customer', default=False)

    @api.multi
    def action_nrg_demo_to_sale(self):
        for quant in self:
            quant.nrg_demo_is_demo = False
        

class ExtendedStockPicking(models.Model):
    """ Inherits stock.picking and ... """
    _inherit = "stock.picking"
    
    # Override
    @api.multi
    def do_new_transfer(self):
        super(ExtendedStockPicking, self).do_new_transfer()
         
        for pick in self:
            sale = self.env['sale.order'].browse(pick.sale_id.id)
            if sale and sale.nrg_demo_is_demo:
                for ops in pick.pack_operation_ids:
                    for opslot in ops.pack_lot_ids:
                        lot = self.env['stock.production.lot'].browse(opslot.lot_id.id)
                        for quant in lot.quant_ids:
                            if not quant.nrg_demo_is_demo:
                                if not quant.nrg_demo_at_customer:
                                    # In the case of transfer to customer.
                                    quant.nrg_demo_is_demo = True
                                    nrg_demo_at_customer = True
                                else:
                                    # In the case of reverse after sale transfer.
                                    quant.nrg_demo_is_demo = False
                                    quant.nrg_demo_at_customer = False
                            else:
                                if quant.nrg_demo_at_customer:
                                    # In the case of reverse of demo.
                                    quant.nrg_demo_is_demo = False
                                    quant.nrg_demo_at_customer = False
