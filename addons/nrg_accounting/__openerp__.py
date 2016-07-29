{
    'name': '[NRG] Accounting',
    'description': 'Customize accounting.',
    'author': 'Shoy',
    'depends': ['sale', 'account', 'crm'],
    'Application': True,
    'data': [
        'sale_view.xml',
        'res_config_view.xml',
        # default data
        'data/accounting_paytypes.xml',
        'data/accounting_paytype_funds.xml',
        'data/account_account_defaults.xml',
        # security
        'security/ir.model.access.csv',
    ],
}
