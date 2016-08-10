# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedPartner(models.Model):
    """ Inherits partner and adds village information in the partner form """
    _inherit = 'res.partner'
    nrg_village = fields.Many2one('nrg.village', 'Village')
    nrg_village_is_keyperson = fields.Boolean('Key Person')
    #Useless because we can find the village from where the customer is
    nrg_village_customer_number = fields.Integer() #--> Replace Integer by Char if we want to be able to find people with a portion of their customer number

    nrg_village_image1 = fields.Binary('Image1')
    nrg_village_image2 = fields.Binary('Image2')
    nrg_village_image3 = fields.Binary('Image3')

    nrg_village_ref_village_place = fields.Char('Province / District / Commune', compute='_compute_village_place')

    """
    # added by Sejin
    # how many people in the household
    nrg_customer_num_of_ppl=fields.Integer('Number of people in the household')
    # what electricity solution they use now

    nrg_customer_solution = fields.Selection([
                 ('Grid', 'Grid'),
                 ('Diesel', 'Diesel'),
                 ('Solar', 'Solar'),
                 ('Unknown','Unknown'),
                 ], string = "Current Electricity Solution", help = "What electricity solution they use now", default = "Unknown", required = True)
    # their current status
    nrg_customer_status = fields.selection([
                ('Active','Active'),
                ('Lost Customer', 'Lost Customer'),
                ('Interested', 'Interested'),
                ('Not Interested', 'Not Interested')
                ('Unknown', 'Unknown'),
                ], string = "Current Status", help = "The customer's current status", default = "Unknown", required = True)
    # their reason for not buying
        # Probably needs another model that stores reasons?
    # nrg_customer_reason = fields.Many2Many"""

    #original
    @api.one
    @api.depends('nrg_village')
    def _compute_village_place(self):
        self.nrg_village_ref_village_place = self.nrg_village and "( " \
                                                + (self.nrg_village.province and self.nrg_village.province.name or "NO PROVINCE") + " / " \
                                                + (self.nrg_village.district and self.nrg_village.district.name or "NO DISTRICT") + " / " \
                                                + (self.nrg_village.commune and self.nrg_village.commune.name or "NO COMMUNE") + " )" or ""
