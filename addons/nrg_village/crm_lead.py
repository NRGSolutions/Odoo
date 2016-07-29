# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedLead(models.Model):
    """ Inherits crm.lead and adds village information in the partner form """
    _inherit = 'crm.lead'
    nrg_village = fields.Many2one('nrg.village', 'Village')
    nrg_village_is_keyperson = fields.Boolean('Key Person')
    
    nrg_village_image1 = fields.Binary('Image1')
    nrg_village_image2 = fields.Binary('Image2')
    nrg_village_image3 = fields.Binary('Image3')
    
    nrg_village_ref_village_place = fields.Char(string='Province / District / Commune', compute='_compute_village_place')

    # Added by Sejin
    # nrg_customer_num_of_ppl=fields.Integer('Number of people in the household')

    @api.one
    def _compute_village_place(self):
        self.nrg_village_ref_village_place = self.nrg_village and "( " \
                                                + (self.nrg_village.province and self.nrg_village.province.name or "NO PROVINCE") + " / " \
                                                + (self.nrg_village.district and self.nrg_village.district.name or "NO DISTRICT") + " / " \
                                                + (self.nrg_village.commune and self.nrg_village.commune.name or "NO COMMUNE") + " )" or ""

    # Override
    def _lead_create_contact(self, cr, uid, lead, name, is_company, parent_id=False, context=None):
        partner_id = super(ExtendedLead, self)._lead_create_contact(cr, uid, lead, name, is_company, parent_id, context)
        partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
        
        partner.nrg_village = lead.nrg_village
        partner.nrg_village_is_keyperson = lead.nrg_village_is_keyperson
        partner.nrg_village_image1 = lead.nrg_village_image1
        partner.nrg_village_image2 = lead.nrg_village_image2
        partner.nrg_village_image3 = lead.nrg_village_image3
                
        return partner_id
