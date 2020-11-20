# -*- coding: utf-8 -*-
{
    'name': "payroll_aze",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ERPGO",
    'website': "https://erpgo.az",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                'base', 
                'hr_worked_days',
                'hr_payslip_monthly_report'
                ],

    # always loaded
    'data': [
#         'security/ir.model.access.csv',
        'views/hr_contract.xml',
        'views/hr_employee.xml',
        'data/hr_salary_rule_category.xml',
        'data/hr.salary.rule.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
