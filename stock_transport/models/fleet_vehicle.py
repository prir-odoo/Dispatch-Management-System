from odoo import fields, models

class FleetCategory(models.Model):

    # specify from which model we want to inherit 
    _inherit = "fleet.vehicle"

    # # field adding
    # max_weight = fields.Char(string="Max Weight", related="fleet_vehicle.model.category.max_weight")
    # max_volume = fields.Char(string="Max Volume", related="fleet.vehicle.model.category.max_volume")
