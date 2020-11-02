from odoo import models, fields, api
from datetime import date, datetime

class HREmployeeExperience(models.Model):
    _name = 'hr.employee.experience'
    _description = 'Employee work experience'
    
    name = fields.Char(string="Company name", required=True)
    employee_id = fields.Many2one('hr.employee',string="Employee", required=True)
    date_from = fields.Date(string="Start date:", required=True)
    date_to = fields.Date(string="End date:")
    current = fields.Boolean(string="Current Employer")
    

class HREmployeeInherit(models.Model):
    _inherit = "hr.employee"

    work_experience_ids = fields.One2many('hr.employee.experience', 'employee_id', string="Work Experience")
    
