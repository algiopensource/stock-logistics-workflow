# -*- coding: utf-8 -*-
# Copyright 2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Auto-assignation of lots on pickings',
    'version': '10.0.1.0.0',
    'author': 'Tecnativa,'
              'Odoo Community Association (OCA)',
    'category': 'Inventory, Logistics, Warehousing',
    'license': 'AGPL-3',
    'website': 'https://www.tecnativa.com',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_picking_type_view.xml',
    ],
    'installable': True,
}
