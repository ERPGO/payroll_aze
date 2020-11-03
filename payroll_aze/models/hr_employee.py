from odoo import models, fields, api
from datetime import date, datetime

class HREmployeeInherit(models.Model):
    _inherit = "hr.employee"

    current_experience = fields.Float(string="Current experience",digits=(12,2), compute="_calculate_current_experience")
    
    def _calculate_current_experience(self):
        for rec in self:
            contracts = self.env['hr.contract'].search([('employee_id','=', rec.id),('state', 'in', ('open','close'))])
            if contracts:
                oldest_contract = contracts.sorted(key=lambda r: r.date_start)[0]
                experience_in_days = (date.today() - oldest_contract.date_start).days
                exp_in_years = experience_in_days / 365
                rec.current_experience = exp_in_years
            else:
                rec.current_experience = 0