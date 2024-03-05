from odoo import models, fields,api

class Inherit(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string="Max Weight (Kg)")
    max_volume = fields.Float(string="Max Weight (m3))")
    
    @api.depends('max_volume','max_weight')
    def _compute_display_name(self):
        for record in self:
            name= record.name
            if record.max_volume or record.max_weight:
                name=f"{name} ({record.max_volume},{record.max_weight})"

            else:
                name= f"{name} (NA,NA)"

            record.display_name=name

    