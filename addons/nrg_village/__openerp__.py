{
    'name': '[NRG] Village Management',
    'description': 'Manage information of villages.',
    'author': 'Shoy',
    'depends': ['crm', 'sale'],
    'Application': True,
    'data': [
        'village_view.xml',
        'res_partner_view.xml',
        'crm_lead_view.xml',
        # default data
        'data/village_event_types.xml',
        'security/ir.model.access.csv',
    ],
}
