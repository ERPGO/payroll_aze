from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class HRLeaveInherit(models.Model):
    _inherit = 'hr.leave'
    
    @api.onchange('date_from', 'date_to', 'employee_id')
    def _onchange_leave_dates(self):
        if self.date_from and self.date_to:
            self.number_of_days = abs(self.date_to - self.date_from + relativedelta(days=+1)).days
        else:
            self.number_of_days = 0
