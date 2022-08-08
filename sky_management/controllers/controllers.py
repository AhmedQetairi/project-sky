# -*- coding: utf-8 -*-
# from odoo import http


# class SkyManagement(http.Controller):
#     @http.route('/sky_management/sky_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sky_management/sky_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sky_management.listing', {
#             'root': '/sky_management/sky_management',
#             'objects': http.request.env['sky_management.sky_management'].search([]),
#         })

#     @http.route('/sky_management/sky_management/objects/<model("sky_management.sky_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sky_management.object', {
#             'object': obj
#         })
