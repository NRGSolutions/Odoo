# -*- coding: utf-8 -*-
{
    'name': '[Sejin] To-do App',

    # 'summary': '',

    'description': 'Manage to-do of the user',

    'author': "Sejin Park",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    # 'category': 'Uncategorized',
    # 'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    'application': True,
    # always loaded
    'data': ['todo_view.xml'],
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    # ],
    # only loaded in demonstration mode
    #'demo': [
      #  'demo/demo.xml',
    #],
}