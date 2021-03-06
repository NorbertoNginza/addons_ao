# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import models

from openerp import SUPERUSER_ID
 
def load_translations(cr, registry):
    chart_template = registry['ir.model.data'].xmlid_to_object(cr, SUPERUSER_ID, 'l10n_ao.l10n_ao_chart_template')
    chart_template.process_coa_translations()
