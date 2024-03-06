from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean(string='Stock Management')