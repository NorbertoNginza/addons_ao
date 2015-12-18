# -*- coding: utf-8 -*-
{
    'name': "Account Parent",
    'summary': """
        This module adds field to specify parent account and also view type account""",
    'description': """
        This module adds field to specify parent account in account and also type 'view' in account type
    """,

    'author': 'ThinkOpen Solutions Angola',
    'website': 'http://www.thinkopensolutions.co.ao',
    'category': 'Accounting &amp; Finance',
    'version': '0.2',
    'depends': ['account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_view.xml',
        'data/account_type_data.xml',
    ],
    'demo': [
#         'demo.xml',
    ],
}