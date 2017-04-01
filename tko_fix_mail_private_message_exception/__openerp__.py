# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    Thinkopen - Portugal & Brasil
#    Copyright (C) Thinkopen Solutions (<http://www.thinkopensolutions.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Fix Mail Private Message Exception',
    'version': '8.0.0.0',
    'category': 'Base',
    'complexity': 'normal',
    'description': ''' Fix Routing: posting a message without model should be with a parent_id (private mesage). ''',
    'author': 'ThinkOpen Solutions',
    'website': 'https://www.tkobr.com',
    'depends': [
        'mail',
    ],
    'data': [
    ],
    'init_xml': [],
    'demo_xml': [],
    'installable': True,
    'application': False,
    'certificate': '',
    'auto_install': False,
}
