{
    'name': "Stock Transport",
    "author": "Prince Rakholiya",
    "depends":['base', 'fleet', 'stock_picking_batch'],
    "data": [
        'security/ir.model.access.csv',
        'views/fleet_category_views.xml',
        'views/stock_picking_batch_view.xml',
        'views/inventory_dock_view.xml',
        'views/stock_picking_view.xml',
        'views/res_config_settings_view.xml'
        # 'views/fleet_vehicle_view.xml',
        ],
    "application": True
}