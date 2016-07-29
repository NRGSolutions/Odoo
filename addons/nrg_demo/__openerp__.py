{
    'name': '[NRG] Demo Process',
    'description': 'Add Demo status in the sales process.',
    'author': 'Shoy',
    'depends': ['sale_stock', 'stock', 'account'],
    'Application': True,
    'data': [
        'sale_view.xml',
        'stock_view.xml',
        'res_config_view.xml',
        'security/ir.model.access.csv',
    ],
}