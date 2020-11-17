# -*- coding: utf-8 -*-
from odoo import http


class ProductApi(http.Controller):
    @http.route('/product_api/product_api/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/product_api/product_api/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('product_api.listing', {
            'root': '/product_api/product_api',
            'objects': http.request.env['product_api.product_api'].search([]),
        })

    @http.route('/product_api/product_api/objects/<model("product_api.product_api"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('product_api.object', {
            'object': obj
        })
