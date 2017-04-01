# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Lorenzo Battistini <lorenzo.battistini@agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

import logging
from openerp import tools, SUPERUSER_ID
from openerp.osv import osv

_logger = logging.getLogger(__name__)


class mail_thread(osv.AbstractModel):
    _inherit = 'mail.thread'

    def get_matching_alias(self, cr, uid, route, email_server_name, context=None):
        # 4. Look for a matching mail.alias entry
        mail_alias = self.pool.get('mail.alias')
        alias_ids = mail_alias.search(cr, uid, [('alias_name', '=', email_server_name.split('@')[0].lower())])
        if alias_ids:
            for alias in mail_alias.browse(cr, uid, alias_ids, context=context):
                if not alias.alias_model_id.model and not alias.alias_force_thread_id:
                    _logger.info('No matching model for the alias %s', alias.alias_name)
                else:
                    user_id = alias.alias_user_id.id
                    if not user_id:
                        user_id = SUPERUSER_ID
                    route = (alias.alias_model_id.model, alias.alias_force_thread_id,
                             eval(alias.alias_defaults), user_id, alias)
                    _logger.info(
                        'Routing mail with no route from %s to %s with direct alias match: %r',
                        email_server_name, alias.alias_name, route)
        return route

    def message_route_verify(
        self, cr, uid, message, message_dict, route, update_author=True,
        assert_model=True, create_fallback=True, allow_private=False,
        context=None
    ):
        # If mail_route() fallback in scenario 5 instead raising an exception
        # we will try to deliver the message to the alias matching the incoming server.
        # One should create an alias with same name as incoming email server
        # set Aliased Model and Record Thread ID, also set Owner to a user with permissions
        # to create the record, if no Owner set we will create it as super user
        model, thread_id, alias = route[0], route[1], route[4]
        # Route doesn't have model neither parent_id
        if not model and not message_dict.get('parent_id'):
            fetchmail_server_id = context.get('fetchmail_server_id')
            fetchmail_server = self.pool['fetchmail.server'].browse(
                cr, uid, fetchmail_server_id, context)
            route = self.get_matching_alias(cr, uid, route, fetchmail_server.user, context=context)
        res = super(mail_thread, self).message_route_verify(
            cr, uid, message, message_dict, route,
            update_author=update_author, assert_model=assert_model,
            create_fallback=create_fallback, allow_private=allow_private,
            context=context)
        return res
