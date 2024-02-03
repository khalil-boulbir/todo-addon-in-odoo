# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'To Do Addons',
    'version': '1.0',
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo.xml',

    ],
    'assets':{

        'web.assets_backend':['todo_management/static/src/css/statusbars.css']

    },
    'application': True,  # Set this to True to make it an application
    'installable': True, 
    'license': 'LGPL-3',
}


