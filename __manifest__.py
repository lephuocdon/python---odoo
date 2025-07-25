{
    'name': 'Real Estate Advertisement',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties and offers',
    'depends': ['base'],
    'data': [
    'views/estate_property_views.xml',
    'views/estate_property_type_views.xml',
    'views/estate_property_tag_views.xml',
    'views/estate_property_offer_views.xml',
    'views/estate_menus.xml',
    'security/ir.model.access.csv',
],

    'application': True,
    'installable': True,
}
