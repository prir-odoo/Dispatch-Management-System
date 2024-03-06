from odoo import fields, models,api

class StockPickingBatch(models.Model):

    # specify from which model we want to inherit 
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("inventory.dock", string="Dock")
    vehicule_id = fields.Many2one("fleet.vehicle", string="Vehicule")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")
    
    weight = fields.Float(string="Weight", compute="_compute_weight", readonly=True, store=True)
    volume = fields.Float(string="Volume", compute="_compute_volume", readonly=True, store=True)
    transfer_count = fields.Float(string="Transfers", compute="_compute_transfer_count", store=True)
    lines_count = fields.Float(string="Lines", compute="_compute_lines", store=True)

    @api.depends("picking_ids.weight_picking", "vehicle_category_id")
    def _compute_weight(self):
        for record in self:
            total_weight = sum(p.weight_picking for p in record.picking_ids)
            max_weight = record.vehicle_category_id.max_weight
            record.weight = (total_weight / max_weight)*100 if max_weight != 0 else 0.0


    @api.depends("picking_ids.volume_picking", "vehicle_category_id")
    def _compute_volume(self):
        for record in self:
            total_volume = sum(p.volume_picking for p in record.picking_ids)
            max_volume = record.vehicle_category_id.max_volume
            record.volume = (total_volume / max_volume)*100 if max_volume != 0 else 0.0

    @api.depends('picking_ids')
    def _compute_transfer_count(self):
        for record in self:
            record.transfer_count = len(record.picking_ids)
    
    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            record.lines_count = len(record.move_line_ids)

    @api.depends('weight' , 'volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + " (" + str(record.weight) + "kg, " + str(record.volume) + "m\u00b3)"

    
    
