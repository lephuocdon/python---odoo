{
    'name': 'Real Estate Advertisement',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties and offers',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/estate_property_views.xml',
    'views/estate_menus.xml',
],

    'application': True,
    'installable': True,
}
