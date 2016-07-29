# -*- config: utf-8 -*-
from openerp import models, fields, api, _, SUPERUSER_ID
from openerp.exceptions import UserError

from datetime import datetime
import os
import re
import pytz
import base64

class ExtendedStockQuant(models.Model):
    """ Inherits stock.quant and adds PAYG IDs management. """
    _inherit = "stock.quant"

    nrg_payg = fields.One2many(
                    'nrg.payg',
                    'nrg_payg_product',
                    'Pay-As-You-Go',
               )
    
    nrg_payg_ref_is_payg = fields.Boolean(string='Is PAYG', related='product_id.product_tmpl_id.nrg_payg_is_payg')
    nrg_payg_tmp_file = fields.Binary('Import File')

    @api.one
    def import_file(self):
        """ Import PAYG codes from a text file. """
        if not self.nrg_payg_tmp_file:
            raise UserError(_('Select a file to import.'))

        text = base64.b64decode(self.nrg_payg_tmp_file)
        if not 'Codegenerator' in text:
            raise UserError(_('Selected file is not correct.'))        
        
        param_list = filter(lambda x: x!='', text.splitlines())
        date = param_list[param_list.index('Date') + 1]
        time = param_list[param_list.index('Time') + 1]
        client = param_list[param_list.index('Client') + 1]
        payment = param_list[param_list.index('Payment') + 1]
        install_code = param_list[param_list.index('Installcode') + 1]
        codes = param_list[param_list.index('Codes') + 1 : len(param_list)]
        for i,code in enumerate(codes):
            codes[i] = re.sub(r'^\d+\s', '', code)

        new_credit_codes = []
        for i,code in enumerate(codes):
            new_credit_codes.append(self.env['nrg.payg.id'].create({
                                        'nrg_payg_id_index': i + 1,
                                        'nrg_payg_id_id': code,
                                    }).id)
        
        tz = pytz.timezone(self.env['res.users'].browse(SUPERUSER_ID).partner_id.tz) or pytz.utc
        new_payg = self.env['nrg.payg'].create({
                        'nrg_payg_product': self.id,
                        'nrg_payg_name': 'IMPORTED ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S'),
                        'nrg_payg_date': tz.localize(datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')).astimezone(pytz.utc),
                        'nrg_payg_client': client,
                        'nrg_payg_payment': payment,
                        'nrg_payg_initial_code': install_code,
                        'nrg_payg_unlock_code': '',
                        'nrg_payg_credit_codes': [(6, 0, new_credit_codes)],
                   })    
