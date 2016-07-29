{
    'name': '[NRG] PAYG ID Management',
    'description': """
Manage Pay-As-You-Go IDs for products.
    """,
    'author': 'Shoy',
    'depends': ['product', 'stock', 'web'],
    'Application': True,
    'data': [
        'stock_view.xml',
        'payg_view.xml',
        'product_view.xml',
        # Default data
        'security/ir.model.access.csv',
    ],
}
