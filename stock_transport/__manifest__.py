{
    'name': 'stock_transport',
    'version': '1.2',
    'summary': 'Transport mnagement System',
    'sequence': 1,
    'description':"Transport mnagement System",
    'category':'Sales/CRM',
    
  'depends': ['base', 'stock_picking_batch','fleet','stock_delivery'],
    'data': [
        "security/ir.model.access.csv",
        "views/batch_transfer.xml",
       "views/fleet_cat.xml",
       
       
       
       "views/add_volume.xml",
    ],
    'demo':[],
    'installable':True,
    'application':True,
    'auto_install':False,
    'licence':'LGPL-3'

}