from odoo import fields, models,api

class StockPicking(models.Model):

    # specify from which model we want to inherit 
    _inherit = "stock.picking"

    volume_picking = fields.Float(string = "Volume", compute="_compute_volume_picking", readonly = True)
    weight_picking = fields.Float(string = "weight", compute="_compute_weight_picking", readonly = True)

    @api.depends("move_ids")
    def _compute_volume_picking(self):
        for record in self:
            record.volume_picking = sum(m.product_id.volume * m.quantity for m in record.move_ids if m.product_id and m.product_id.volume)
    
    @api.depends("move_ids")
    def _compute_weight_picking(self):
        for record in self:
            record.weight_picking = sum(m.product_id.weight * m.quantity for m in record.move_ids if m.product_id and m.product_id.weight)
            

    
