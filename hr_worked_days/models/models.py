# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class PayslipInherit(models.Model):
    _inherit = 'hr.payslip'
    
    working_days = fields.Float("Working days", readonly=True, compute="_compute_working_days")
    
    def _compute_working_days(self):
        now = self.date_from
        businessdays = 0
        holidays = []
        global_leaves = self.contract_id.resource_calendar_id.global_leave_ids
        for leave in global_leaves:
            start_date = leave.date_from.date()
            end_date = leave.date_to.date()
            delta = end_date - start_date
            numdays = delta.days
            date_list = []
            for x in range (0, numdays):
                date_list.append(end_date - datetime.timedelta(days = x))
            date_list.append(start_date)
            holidays.extend(date_list)
        for i in range(1, 32):
            try:
                thisdate = datetime.date(now.year, now.month, i)
            except Exception:
                break
            if thisdate.weekday() < 5 and thisdate not in holidays:
                businessdays += 1
        self.working_days = businessdays

    
    