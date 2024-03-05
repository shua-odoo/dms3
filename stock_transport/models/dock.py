# from odoo import models, fields,api

# class dock(models.Model):
#     _name= "docks"
#     _description="This is docks data"
#     dock= fields.Selection(
#         selection=[
#             ("docka", "Dock A"),
#             ("dockb", "Dock B"),
#             ("dockc", "Dock C"),
#             ("dockd", "Dock D"),
#             ("docke", "Dock E"),
#         ])

from odoo import fields, models


class ModelDock(models.Model):
    _name = "model.dock"
    _description = "Dock"

    name = fields.Char("Name", required=True)

    

    
