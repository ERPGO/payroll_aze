# -*- coding: utf-8 -*-
{
    'name': "Payslip Working days",
    'version': '0.1',
    'depends': [
        'base',
        'hr_payroll_community'
        ],
    'author': "ERPGO",
    'category': 'Uncategorized',
    'summary': """Calculate working days excluding leaves in payslip""",
    'description': """
        Calculation of working days
        Calculates the number of working days for a selected month in the payslip calculation.
        Some use cases where this module can be useful:
            *an employee hasn't worked the whole month and his basic pay needs to be prorated based on the actual worked days out of total worked days
            
            *use working days information for calculation in any other salary rule
        
        A float field has been added to the payslip form view which is calculating the working 
        days in respective working schedule of an employee by talking out the respective global
        leaves.""",
    'website': "http://www.erpgo.az",
    # always loaded
    'data': [
        'views/views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    
}
