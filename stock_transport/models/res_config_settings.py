from odoo import fields, models,api

class ResConfigSettings(models.Model):

    # specify from which model we want to inherit 
    _inherit = "res.config.settings"

    module_stock_transport = fields.Boolean("Dispatch management System",
        help="abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

    
