# -*- encoding: utf-8 -*-

{
    'name': 'TKO Compose Mail',
    'version': '11.0',
    'price': 8.0,
    'category': 'Discuss',
    'sequence': 150,
    'complexity': 'normal',
    'description': '''  This module allows to compose email from anywhere in the odoo,
    It is like compose button in gmail''',
    'author': 'ThinkOpen Solutions Brasil',
    'website': 'http://www.tkobr.com',
    'images': [
    ],
    'qweb': ['static/src/xml/*.xml'],
    'depends': [
        'mail'
    ],
    'data': [
        'views/assets.xml'
    ],
    'init': [],
    'demo': [],
    'update': [],
    'test': [],  # YAML files with tests
    'installable': True,
    'application': False,
    'auto_install': False,
    'certificate': '',
}
