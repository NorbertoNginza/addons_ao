# -*- coding: utf-8 -*-
from openerp import api, fields, models, _

class AccountAccountType(models.Model):
    _inherit = "account.account.type"
    type = fields.Selection([
        ('view', 'View'),
        ('other', 'Regular'),
        ('receivable', 'Receivable'),
        ('payable', 'Payable'),
        ('liquidity', 'Liquidity'),
    ], required=True, default='other',
        help="The 'Internal Type' is used for features available on "\
        "different types of accounts: liquidity type is for cash or bank accounts"\
        ", payable/receivable is for vendor/customer accounts.")

class AccountAccount(models.Model):
    _inherit = "account.account"
    
    parent_id = fields.Many2one('account.account','Parent Account')
    child_ids = fields.One2many('account.account','parent_id', 'Child Accounts')
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        context = self._context or {}
        if not context.get('show_parent_account',False):
            args += [('user_type_id.type', '!=', 'view')]
        return super(AccountAccount, self).search(args, offset, limit, order, count=count)
