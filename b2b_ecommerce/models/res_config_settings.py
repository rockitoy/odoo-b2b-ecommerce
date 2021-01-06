# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2021. All rights reserved.

from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    b2b_hide_price = fields.Boolean('Hide price from not logged-in users')
    b2b_hide_add_cart = fields.Boolean('Hide Add to Cart selection from not logged-in users')
    b2b_hide_common_text = fields.Boolean(
        'Hide money back gaurantee and other common promises from not logged-in users')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()

        res.update(
            b2b_hide_price=params.get_param('b2b_ecommerce.b2b_hide_price', default=False),
            b2b_hide_add_cart=params.get_param('b2b_ecommerce.b2b_hide_add_cart', default=False),
            b2b_hide_common_text=params.get_param('b2b_ecommerce.b2b_hide_common_text', default=False),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('b2b_ecommerce.b2b_hide_price', self.b2b_hide_price)
        self.env['ir.config_parameter'].sudo().set_param('b2b_ecommerce.b2b_hide_add_cart', self.b2b_hide_add_cart)
        self.env['ir.config_parameter'].sudo().set_param('b2b_ecommerce.b2b_hide_common_text',
                                                         self.b2b_hide_common_text)
