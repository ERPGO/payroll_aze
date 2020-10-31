# -*- coding: utf-8 -*-
# from odoo import http


# class PayrollAze(http.Controller):
#     @http.route('/payroll_aze/payroll_aze/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payroll_aze/payroll_aze/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payroll_aze.listing', {
#             'root': '/payroll_aze/payroll_aze',
#             'objects': http.request.env['payroll_aze.payroll_aze'].search([]),
#         })

#     @http.route('/payroll_aze/payroll_aze/objects/<model("payroll_aze.payroll_aze"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payroll_aze.object', {
#             'object': obj
#         })
