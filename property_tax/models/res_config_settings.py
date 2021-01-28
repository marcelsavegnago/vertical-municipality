from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    property_tax_fixed_value = fields.Float('Fixed Value', config_parameter='property_tax.fixed_value')
    property_tax_minimal_contribution = fields.Float('Minimal Contribution', config_parameter='property_tax.minimal_contribution')
    property_tax_formula = fields.Char('Formula', config_parameter='property_tax.formula')