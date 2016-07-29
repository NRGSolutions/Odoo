{
    'name': '[NRG] ACL Customization',
    'description': 'Access controls for local managers and staffs.',
    'author': 'Shoy',
    'depends': ['stock', 'nrg_village'],
    'Application': True,
    'data': [
        'res_users_view.xml',
        'res_partner_view.xml',
        'sale_view.xml',
        'stock_view.xml',
        'security/nrg_acl_security.xml',
    ],
}
