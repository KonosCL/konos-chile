# -*- coding: utf-8 -*-
# Init module for l10n_cl_base
# Daniel Blanco - Blanco Martin & Asociados
##############################################################################
'''This code intended to define transient fields for installing modules'''
from openerp import models, fields


class konos_base_configuration(models.TransientModel):
    '''Inherit Odoo base config'''
    _name = 'konos.base.config.settings'
    _inherit = 'res.config.settings'



    module_l10n_cl_dte = fields.Boolean(
        'DTE Chile',
        help="""Installs module module_l10n_cl_dte, and all DTE requirements.""")

    module_l10n_cl_dte_caf = fields.Boolean(
        'DTE CAF',
        help="""Installs module module_l10n_cl_dte_caf, and all DTE requirements.""")

    module_l10n_cl_dte_factoring = fields.Boolean(
        'DTE Factoring',
        help="""Installs module l10n_cl_dte_factoring, and all DTE requirements.""")

    module_l10n_cl_stock_picking = fields.Boolean(
        'Guías de Despacho Electrónicas',
        help="""Installs module l10n_cl_stock_picking, and all DTE requirements.""")


    module_l10n_cl_dte_point_of_sale = fields.Boolean(
        'DTE Point of Sales',
        help="""Installs module 10n_cl_dte_point_of_sale, and all DTE requirements.""")



    module_l10n_cl_counties = fields.Boolean(
        'Counties in Chile',
        help="""Installs module l10n_cl_counties, and all counties in Chile.""")


    module_l10n_cl_banks_sbif = fields.Boolean(
        'Banks in Chile, According SBIF',
        help="""Installs module l10n_cl_banks_sbif, and includes authorized
banks, and financial institutions in Chile.""")

    module_l10n_cl_chart_of_account = fields.Boolean(
        'Chart of Accounts SII',
        help="""Installs module l10n_cl_chart_of_account, and includes authorized
chart of accounts in Chile.""")


    module_l10n_cl_libro_compra_venta = fields.Boolean(
        'Sales and Purchases Books',
        help="""Installs module  l10n_cl_libro_compra_venta, and includes authorized
chart of accounts in Chile.""")



    module_l10n_cl_financial_indicators = fields.Boolean(
        'Update UF, UTM, Dollar and Euro automatically',
        help="""Installs module l10n_cl_financial_indicators, allowing to
update indicators daily, from SBIF.""")


    module_l10n_cl_invoice = fields.Boolean(
        'Allows to have your stubs presented to the same sales journal',
        help="""Installs l10n_cl_invoice Link your invoicing, picking and
receipts stubs with journals for easiest configuration.""")



    module_l10n_cl_partner_activities = fields.Boolean(
        'Include Partner\'s Businness Activities', help="""Installs l10n_cl_partner_activities
module, which includes your partners' turns in their record using the SII
activities table and allows you to select the activity when invoicing.""")

    module_l10n_cl_hr_payroll = fields.Boolean(
        'Install payroll and AFPs chilean modules',
        help="""Install l10n_cl_hr_payroll for payroll and AFPs chilean
modules""")


    module_l10n_cl_base_rut = fields.Boolean(
        'Validate Chilean VAT (RUT) and format to 99.999.999-X',
        help="""Installs l10n_cl_base_rut in ordar to validate de VAT (RUT) \
        ant to have it formatted correctly, according Chilean usage.""")


    module_base_currency_inverse_rate = fields.Boolean(
        'Base Currency Inverse Rate',
        help="""Installs base_currency_inverse_rate.""")

    module_decimal_precision = fields.Boolean(
        'Decimal Precision',
        help="""Installs decimal_precision in ordar to validate de VAT (RUT) \
        ant to have it formatted correctly, according Chilean usage.""")

    module_decimal_precision_currency = fields.Boolean(
        'Decimal Precision Currency',
        help="""Installs module_decimal_precision_currency.""")
    
    module_mass_editing = fields.Boolean(
        'Mass Editing',
        help="""Installs module_mass_editing.""")

    module_global_discount = fields.Boolean(
        'Global Discount',
        help="""Installs module_global_discount.""")
    
    module_account_cancel = fields.Boolean(
        'Account Cancel',
        help="""Installs module_account_cancel.""")

    module_web_export_view = fields.Boolean(
        'Excel Export',
        help="""Installs module_web_export_view.""")
    
    module_account_payment_group = fields.Boolean(
        'Payment Group',
        help="""Installs module_account_payment_group.""")


