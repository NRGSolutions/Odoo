# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError

class NrgVillage(models.Model):
    _name = 'nrg.village'
    _description = ''

    province = fields.Many2one('nrg.village.province', 'Province')
    district = fields.Many2one('nrg.village.district', 'District', domain="[('parent_province', '=', province)]")
    commune = fields.Many2one('nrg.village.commune', 'Commune', domain="[('parent_district', '=', district)]")
    name = fields.Char('Village', required=True, index=True)
    
    is_active = fields.Boolean('Is Active', default=True)
    num_of_households = fields.Integer('Number of Households')
    num_of_households_w_solar = fields.Integer('Number of Households Using Solar')
    
    events = fields.One2many(
        'nrg.village.event',
        'village',
        'Events'
    )
    
    village_leads = fields.One2many(
        'crm.lead',
        'nrg_village',
        'Leads',
        domain=[('partner_id', '=', False)]
    )
    village_customers = fields.One2many(
        'res.partner',  # related model
        'nrg_village',  # field for "this" on related model
        'Customers'
    )
    note = fields.Text('Note')
    image1 = fields.Binary('Image1')
    image2 = fields.Binary('Image2')
    image3 = fields.Binary('Image3')
    
    meeting_count = fields.Integer(compute='_compute_meeting_count')
    sale_order_count = fields.Integer(compute='_compute_sale_order_count')

    @api.one
    @api.constrains('num_of_households_using_solar')
    def _check_num_of_households_using_solar_size(self):
        if self.num_of_households_w_solar > self.num_of_households:
            raise ValidationError('Must less than total households!')

    @api.multi
    def schedule_meeting(self):
        self.ensure_one()
        
        res = self.env['ir.actions.act_window'].for_xml_id('calendar', 'action_calendar_event')
        res['context'] = {
            'search_default_partner_ids': self.village_customers.ids,
#             'default_partner_ids': self.village_customers.ids,
            'default_user_id': self.env.uid,
            'default_name': self.name,
        }
#         res['domain'] = []
        
        return res
    
    @api.one
    def _compute_meeting_count(self):
        count = 0
        # the user may not have access rights for meetings
        try:
            for customer in self.village_customers:
                count += len(customer.meeting_ids)
        except:
            pass
        self.meeting_count = count;
        
    @api.multi
    def sale_order(self):
        self.ensure_one()
        
        res = self.env['ir.actions.act_window'].for_xml_id('nrg_village', 'action_village_2_sale_order')
        res['context'] = {
#             'search_default_partner_id': self.village_customers.ids[0],
            'default_user_id': self.env.uid,
            'default_name': self.name,
        }
        res['domain'] = [('partner_id', 'in', self.village_customers.ids)]
        
        return res
            
    @api.one
    def _compute_sale_order_count(self):
        count = 0
        # the user may not have access rights for sale orders
        try:
            for customer in self.village_customers:
                count += len(customer.sale_order_ids) + len(customer.mapped('child_ids.sale_order_ids'))
        except:
            pass
        self.sale_order_count = count;


class NrgVillageEvent(models.Model):
    _name = 'nrg.village.event'
    _description = ''
    
    name = fields.Char('Name')
    type = fields.Many2one('nrg.village.event.type', 'Type')
    date = fields.Date('Date')
    num_of_people = fields.Integer('Num. of People')
    village = fields.Many2one('nrg.village', 'Village')
    note = fields.Text('Note')


class NrgVillageEventType(models.Model):
    _name = 'nrg.village.event.type'
    _description = ''
    
    name = fields.Char('Name')


class NrgProvince(models.Model):
    _name = 'nrg.village.province'
    _description = ''
#     _parent_store = True
    
    name = fields.Char('Name')
#     parent_id = None
    child_districts = fields.One2many('nrg.village.district', 'parent_province', 'Districts')
#     parent_left = fields.Integer('Parent Left', index=True)
#     parent_right = fields.Integer('Parent Right', index=True)
    

class NrgDistrict(models.Model):
    _name = 'nrg.village.district'
    _description = ''
#     _parent_store = True
     
    name = fields.Char('Name')
#     parent_province = fields.Many2one('nrg.village.province', 'Province', ondelete='restrict')
    parent_province = fields.Many2one('nrg.village.province', 'Province', ondelete='cascade')
    child_communes = fields.One2many('nrg.village.commune', 'parent_district', 'Communes')
#     parent_left = fields.Integer('Parent Left', index=True)
#     parent_right = fields.Integer('Parent Right', index=True)
    
     
class NrgCommune(models.Model):
    _name = 'nrg.village.commune'
    _description =''
#     _parent_store = True
     
    name = fields.Char('Name')
#     parent_district = fields.Many2one('nrg.village.district', 'District', ondelete='restrict')
    parent_district = fields.Many2one('nrg.village.district', 'District', ondelete='cascade')
#     parent_left = fields.Integer('Parent Left', index=True)
#     parent_right = fields.Integer('Parent Right', index=True)

