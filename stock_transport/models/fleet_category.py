from odoo import fields, models

class FleetCategory(models.Model):

    # specify from which model we want to inherit 
    _inherit = "fleet.vehicle.model.category"

    # field adding
    max_weight = fields.Float(string="Max Weight")
    max_volume = fields.Float(string="Max Volume")
    
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + " (" + str(record.max_weight) + "kg, " + str(record.max_volume) + "m\u00b3)"

