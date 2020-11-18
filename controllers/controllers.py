# -*- coding: utf-8 -*-
from odoo import http





class ProductApi(http.Controller):
    @http.route('/api/product', auth='public')
    def index(self, **kw):
        return "Hi,Enter the product ID in the URL"

    @http.route('/api/product/<int:product_id>', auth='public')
    def list(self,product_id, **kw):
        return http.request.render('product_api.listing', {
            'root': '/product_api',
            'objects': http.request.env['product.product'].search([('id','=',product_id)]),
        })
    
    @http.route('/api/product/json/<int:product_id>', auth='public')
    def json_data(self,product_id, **kw):
        data =[]
        product = http.request.env['product.product'].sudo().browse(product_id)
        if not product:
            return False
        
        data.append({'product':product.name,
                    'price':product.list_price,
                    'cost':product.standard_price,
                    'OnHandQty':product.qty_available,
                    'category':product.categ_id.name})

        return data

   
