from odoo import fields, models

class FleetCategory(models.Model):

    # specify from which model we want to inherit 
    _inherit = "fleet.vehicle"
