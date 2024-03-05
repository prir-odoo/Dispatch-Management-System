from odoo import fields, models

class InventoryDock(models.Model):

    _name = "inventory.dock"

    name = fields.Char()

