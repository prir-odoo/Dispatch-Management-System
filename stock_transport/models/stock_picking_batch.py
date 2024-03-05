from odoo import fields, models,api

class StockPickingBatch(models.Model):

    # specify from which model we want to inherit 
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("inventory.dock", string="Dock")
    vehicule_id = fields.Many2one("fleet.vehicle", string="Vehicule")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")
    
    weight = fields.Float(string="Weight", compute="_compute_weight", readonly=True)
    volume = fields.Float(string="Volume", compute="_compute_volume", readonly=True)

    @api.depends("move_line_ids", "vehicle_category_id")
    def _compute_weight(self):
        for record in self:
            total_weight = sum(move_line.product_id.weight * move_line.quantity for move_line in record.move_line_ids if move_line.product_id and move_line.product_id.weight)
            max_weight = record.vehicle_category_id.max_weight
            record.weight = (total_weight / max_weight)*100 if max_weight != 0 else 0.0


    @api.depends("move_line_ids", "vehicle_category_id")
    def _compute_volume(self):
        for record in self:
            total_volume = sum(move_line.product_id.volume * move_line.quantity for move_line in record.move_line_ids if move_line.product_id and move_line.product_id.volume)
            max_volume = record.vehicle_category_id.max_volume
            record.volume = (total_volume / max_volume)*100 if max_volume != 0 else 0.0

    
