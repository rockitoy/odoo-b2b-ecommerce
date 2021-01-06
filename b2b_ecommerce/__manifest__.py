# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2021. All rights reserved.

{
    'name': 'B2B eCommerce',
    'version': '14.0.0.0',
    'category': 'Website',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
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
