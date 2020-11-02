from odoo import models, fields, api

class HRContractInherit(models.Model):
    _inherit = 'hr.contract'

    life_insurance_amount = fields.Monetary('Life Insurance amount', required=True, tracking=True, help="Employee's monthly life insurance amount.")
