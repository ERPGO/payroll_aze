# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

class HRPayslipAze(models.Model):
    _inherit = 'hr.payslip'
    
    timeoff_rate = fields.Float(compute="_calculate_timeoff_rate", string="timeoff rate")
    
    def _calculate_timeoff_rate(self):
        for rec in self:
            employee_payslips = self.search([('employee_id','=',rec.employee_id.id),('state','=','done')])
            date_from = rec.date_from - relativedelta(years=+1)
            date_to = rec.date_from - relativedelta(days=+1)
            pay_set = self.env['hr.payslip']
            for payslip in employee_payslips:
                if date_from < payslip.date_from < date_to:
                    pay_set += payslip
            if pay_set:
                # Remove uncomplete first month for employee from time off calculation
                employee_start_date = rec.contract_id.date_start
                new_set = pay_set
                if employee_start_date.day != 1:
                    for pay in pay_set:
                        if pay.date_from.month == employee_start_date.month:
                            new_set = pay_set - pay
                total_gross = 0
                for pay in new_set:
                    for line in pay.line_ids:
                        if line.code == "GROSS":
                            total_gross += line.total
                rate = total_gross / len(new_set) / 30.4
                rec.timeoff_rate = rate
            else:
                rec.timeoff_rate = 0