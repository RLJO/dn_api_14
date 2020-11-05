# -*- coding: utf-8 -*-
# from odoo import http


# class DnApi14(http.Controller):
#     @http.route('/dn_api_14/dn_api_14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dn_api_14/dn_api_14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dn_api_14.listing', {
#             'root': '/dn_api_14/dn_api_14',
#             'objects': http.request.env['dn_api_14.dn_api_14'].search([]),
#         })

#     @http.route('/dn_api_14/dn_api_14/objects/<model("dn_api_14.dn_api_14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dn_api_14.object', {
#             'object': obj
#         })
