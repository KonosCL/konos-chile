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
        'DTE CAF Folios',
        help="""Installs module module_l10n_cl_dte_caf, and all DTE requirements.""")

    module_l10n_cl_dte_factoring = fields.Boolean(
        'DTE Factoring',
        help="""Installs module l10n_cl_dte_factoring, and all DTE requirements.""")

    module_l10n_cl_stock_picking = fields.Boolean(
        'DTE Guías de Despacho Electrónicas',
        help="""Installs module l10n_cl_stock_picking, and all DTE requirements.""")


    module_l10n_cl_dte_point_of_sale = fields.Boolean(
        'DTE Punto de Venta',
        help="""Installs module 10n_cl_dte_point_of_sale, and all DTE requirements.""")



    module_l10n_cl_counties = fields.Boolean(
        'Comunas de Chile',
        help="""Installs module l10n_cl_counties, and all counties in Chile.""")


    module_l10n_cl_banks_sbif = fields.Boolean(
        'Bancos en Chile',
        help="""Installs module l10n_cl_banks_sbif, and includes authorized
banks, and financial institutions in Chile.""")

    module_l10n_cl_chart_of_account = fields.Boolean(
        'Plan de Cuentas SII',
        help="""Installs module l10n_cl_chart_of_account, and includes authorized
chart of accounts in Chile.""")


    module_l10n_cl_libro_compra_venta = fields.Boolean(
        'Libros de Compra y Ventas',
        help="""Installs module  l10n_cl_libro_compra_venta, and includes authorized
chart of accounts in Chile.""")



    module_l10n_cl_financial_indicators = fields.Boolean(
        'Indicadores Financieros',
        help="""Installs module l10n_cl_financial_indicators, allowing to
update indicators daily, from SBIF.""")


    module_l10n_cl_invoice = fields.Boolean(
        'Facturación Chile',
        help="""Installs l10n_cl_invoice Link your invoicing, picking and
receipts stubs with journals for easiest configuration.""")



    module_l10n_cl_partner_activities = fields.Boolean(
        'Giros en Chile - Actividades', help="""Installs l10n_cl_partner_activities
module, which includes your partners' turns in their record using the SII
activities table and allows you to select the activity when invoicing.""")

    module_l10n_cl_hr_payroll = fields.Boolean(
        'Liquidaciones en Chile',
        help="""Install l10n_cl_hr_payroll for payroll and AFPs chilean
modules""")


    module_l10n_cl_base_rut = fields.Boolean(
        'Formato de RUT 99.999.999-X',
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
        'Edición Masiva',
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

    module_vit_journal_voucher = fields.Boolean(
        'Impresión de Comprobantes Contables',
        help="""Installs vit_journal_voucher.""")

    module_l10n_cl_balance = fields.Boolean(
        'Reportes Contables en Chile',
        help="""Installs module_l10n_cl_balance.""")

    module_layouts_custom = fields.Boolean(
        'Layouts Custom',
        help="""Installs module_layouts_custom.""")

    module_customer_account_followup = fields.Boolean(
        'Seguimiento de Cheques y Pagos',
        help="""Installs module_customer_account_followup.""")

    module_payroll_analytic_account = fields.Boolean(
        'Centros de Costos en Liquidaciones',
        help="""Installs module_payroll_analytic_account.""")

    module_hr_holiday_exclude_special_days = fields.Boolean(
        'Excluye Días Feriados y Fines de Semana',
        help="""Installs module_hr_holiday_exclude_special_days.""")

    module_auth_signup = fields.Boolean(
        'Auth Signup',
        help="""Installs module_auth_signup.""")

    module_auto_backup = fields.Boolean(
        'Auto Backup',
        help="""Installs module_auto_backup.""")

    module_document = fields.Boolean(
        'Documentos Adjuntos',
        help="""Installs module_document.""")
