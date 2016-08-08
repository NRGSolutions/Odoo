# -*- coding: utf-8 -*-

# ------------------------
#  res_partner.py
#  Date: 08/05/2016 
#  Author: Sejin Park
# ------------------------

from openerp import models, fields, api

class ExtendedPartner(models.Model):
	# Inherits partner and adds customer demographics criteria in the partner form
	_inherit = 'res.partner'

	# Customer's primary income and secondary income
	nrg_customer_primary_income = fields.Integer('Primary income')
	nrg_customer_secondary_income = fields.Integer('Secondary income')

	# Household primary income source
	nrg_customer_primary_income_source = fields.Selection([('farming', 'Farming')], 
											string="Primary source of income")

	# Current appliances
	nrg_customer_appliances_fan = fields.Boolean('Fan')
	nrg_customer_appliances_tv = fields.Boolean('TV')
	nrg_customer_appliances_lights = fields.Boolean('Lights')

	# Number of people in the household
	nrg_customer_num_of_ppl = fields.Integer('Number of people in the household')
	
	# Number of rooms in the house
	nrg_customer_num_of_rooms = fields.Integer('Number of rooms in the house')

	# Current energy source
	nrg_customer_energy_source = fields.Selection([('grid', 'Grid'), ('car battery', 'Car Battery'), 
													('generator','Generator')],
												string="Current energy source?")
	# Energy spending per week
	nrg_customer_energy_spending = fields.Integer('Energy spending per week')

	# Main cooking technology
	nrg_customer_cooking_tech = fields.Selection([('charcoal stove', 'Charcoal Stove'), ('LPG', 'LPG')],
												string="Main cooking technology?")

	# Do they want solar? 
	nrg_customer_want_solar = fields.Selection([('yes','Yes'), ('no','No'), ('maybe','Maybe')], 
												string="Do they want solar?")
