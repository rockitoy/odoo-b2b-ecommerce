# -*- coding: utf-8 -*-
# Copyright (C) 2017-present  Technaureus Info Solutions(<http://www.technaureus.com/>).

{
    'name': 'B2B eCommerce',
    'version': '1.0',
    'category': 'Website',
    'sequence': 1,
    'author':'Technaureus Info Solutions Pvt. Ltd.',
    'summary': 'Business to Business Ecommerce',
    'website': 'http://www.technaureus.com/',
    'description': """
This addon will give option to hide the price and 'Add to Cart' button in eCommerce.""",
    'depends': ['website_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
