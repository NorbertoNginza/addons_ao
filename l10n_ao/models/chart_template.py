# -*- coding: utf-8 -*-

from openerp import api, fields, models, _
    
class WizardMultiChartsAccounts(models.TransientModel):
    _inherit = 'wizard.multi.charts.accounts'
    
    @api.multi
    def execute(self):
        if self.chart_template_id.id == self.env.ref('l10n_ao.l10n_ao_chart_template').id:
            self.bank_account_ids = [(6,0,[])]
        return super(WizardMultiChartsAccounts, self).execute()
                
class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"
    
    @api.multi
    def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):
        
        journal_data = super(AccountChartTemplate, self)._prepare_all_journals(acc_template_ref,
                                                            company,journals_dict=journals_dict)
        
        for journal in journal_data:
            if journal['name'] == _('Customer Invoices') and acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_611100').id,False):
                journal['default_credit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_611100').id,False)
                journal['default_debit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_611100').id,False)
            elif journal['name'] == _('Vendor Bills') and acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_212100').id,False):
                journal['default_credit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_212100').id,False)
                journal['default_debit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_212100').id,False)
            elif journal['name'] == _('Exchange Difference') and acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_662100').id,False):
                journal['default_credit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_662100').id,False)
                journal['default_debit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_762100').id,False)
        
        if acc_template_ref.get(self.env.ref('l10n_ao.ao_431101').id,False) and \
                    acc_template_ref.get(self.env.ref('l10n_ao.ao_451101').id,False):
            #this checking is for verifying whether the loading chart is l10n_ao
            journal_data.extend([{
                'type': 'bank',
                'name': _('Bank'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_431101').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_431101').id,False),
#                 'refund_sequence': True,
                'show_on_dashboard': True,
            }, {
                'type': 'cash',
                'name': _('Cash'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_451101').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_451101').id,False),
#                 'refund_sequence': True,
                'show_on_dashboard': True,
            }, {
                'type': 'general',
                'name': _('Sale Debit Notes'),
                'code': _('SCNJ'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_611100').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_611100').id,False),
#                 'refund_sequence': True,
#                 'show_on_dashboard': True,
            }, {
                'type': 'general',
                'name': _('Supplier Debit Notes'),
                'code': _('PCNJ'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_212100').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_212100').id,False),
#                 'refund_sequence': True,
#                 'show_on_dashboard': True,
            },])
        return journal_data