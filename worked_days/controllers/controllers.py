# -*- coding: utf-8 -*-
# from odoo import http


# class DosttechPayslip(http.Controller):
#     @http.route('/dosttech_payslip/dosttech_payslip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dosttech_payslip/dosttech_payslip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dosttech_payslip.listing', {
#             'root': '/dosttech_payslip/dosttech_payslip',
#             'objects': http.request.env['dosttech_payslip.dosttech_payslip'].search([]),
#         })

#     @http.route('/dosttech_payslip/dosttech_payslip/objects/<model("dosttech_payslip.dosttech_payslip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dosttech_payslip.object', {
#             'object': obj
#         })
