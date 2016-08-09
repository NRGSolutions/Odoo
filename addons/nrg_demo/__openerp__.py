{
    'name': '[NRG] Demo Process',
    'description': 'Add Demo status in the sales process.',
    'author': 'Shoy',
    # Line added by Sejin Park on 08/02/2016
    'depends': ['sale_stock', 'stock', 'account', 'calendar'],
    'Application': True,
    'data': [
        'sale_view.xml',
        'stock_view.xml',
        'res_config_view.xml',
        'security/ir.model.access.csv',
        # Line added by Sejin Park on 08/02/2016
        'calendar_event.xml'
    ],
}