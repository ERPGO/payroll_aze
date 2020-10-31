# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

class HRPayslipAze(models.Model):
    _inherit = 'hr.payslip'
    
    timeoff_rate = fields.Float(compute="_calculate_timeoff_rate", string="timeoff rate", store=True)
    
    def _calculate_timeoff_rate(self):
        for rec in self:
            employee_payslips = self.search([('employee_id','=',rec.employee_id.id),('state','=','done')])
            date_from = rec.date_from - relativedelta(years=+1)
            date_to = rec.date_from - relativedelta(days=+1)
            out_payslips = [payslip for payslip in employee_payslips if date_from < payslip.date_from < date_to]
            if out_payslips:
                total_gross = 0
                for pay in out_payslips:
                    for line in pay.line_ids:
                        if line.code == "GROSS":
                            total_gross += line.total
                rate = total_gross / len(out_payslips) / 30.4
                rec.timeoff_rate = rate
            else:
                rec.timeoff_rate = 0