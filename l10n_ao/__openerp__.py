# -*- encoding: utf-8 -*-


{
    'name': 'Angolan - Accounting',
    'version': '0.4',
    'category': 'Localization/Account Charts',
    'description': """
Angolan Accounting Module
=========================

Angolan accounting basic charts and localizations.

Also:
    - activates regional currency.
    - sets up taxes.
    """,
    'author': 'ThinkOpen Solutions Angola',
    'website': 'http://www.thinkopensolutions.co.ao',
    'depends': ['account_parent','l10n_multilang'],
    'data': [
             'data/account_chart_template.xml',
             'data/account.account.template.csv',
             'data/account_chart_template_updated.xml',
#              'data/account_chart_template_refs.xml',
#              'data/account.account.tag.csv',
            'data/account.tax.template.csv',
#              'data/account_fiscal_position_tax_template.xml',
             'data/account_chart_template.yml',
             'data/localisation.xml',
             'data/res.bank.csv',
             'data/res.country.state.csv'
             ],
    'demo': [],
    'installable': True,
    'images': [],
    'post_init_hook': 'load_translations'
}
