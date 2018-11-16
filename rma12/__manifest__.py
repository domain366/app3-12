# -*- coding: utf-8 -*-

{
    "name" : "Website RMA - Return Orders Management/Return Merchandise Authorization",
    "version" : "12.0.0.0",
    "category" : "eCommerce",
    "depends" : ['base','sale','sale_management','website','website_sale','stock'],
    "author": "BrowseInfo",
    'summary': 'This apps allow your customer to manage return of the products & create return RMA order from the website',
    "description": """
    
    Purpose :- 
This Module allow the seller to recharge wallet for the customer. 
    website return order
    website RMA
    eCommerce RMA
    eCommerce return order
    webshop RMA
    webshop return order
    website Return Orders Management
    website Return Merchandise Authorization
    webshop Return Orders Management
    webshop Return Merchandise Authorization
    eCommerce Return Orders Management
    eCommerce Return Merchandise Authorization


    
    """,
    "data": [
        'security/ir.model.access.csv',
        'views/rma_view.xml',
        'views/website_rma.xml',
        'views/rma_order_sequence.xml',
    ],
    "auto_install": False,
    "installable": True,
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
