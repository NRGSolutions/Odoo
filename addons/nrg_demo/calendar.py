# -*- config: utf-8 -*-
from openerp import models, fields, api

class ExtendedCalendar(models.Model):
	_inherit = 'calendar.event'

	nrg_demo_cal_is_template = fields.Boolean('Is Template', default=False, help='Template')