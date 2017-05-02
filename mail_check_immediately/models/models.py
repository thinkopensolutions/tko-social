# -*- coding: utf-8 -*-
import datetime
from pytz import timezone
from openerp.tools.translate import _
from openerp import tools

from openerp import exceptions
from openerp import models, fields, api


class FetchMailServer(models.Model):
    _inherit = 'fetchmail.server'
    _name = 'fetchmail.server'

    _last_updated = None

    run_time = fields.Datetime(string="Launch time")

    def _run_time(self):
        if not self._last_updated:
            self._last_updated = tools.datetime.now()
        dst_tz_name = self._context.get('tz') or self.env.user.tz
        now_utc = datetime.datetime.now(timezone('UTC'))
        now = now_utc.astimezone(timezone(dst_tz_name))
        return now

    @api.model
    def _fetch_mails(self):
        if self._context.get('run_fetchmail_manually'):
            # if interval less than 5 seconds
            if self._last_updated and \
                    (datetime.datetime.now() - self._last_updated) \
                                                    < datetime.timedelta(0, 5):
                raise exceptions.Warning(_('Error'),\
                            _('Task can be started no earlier than 5 seconds.'))

        super(FetchMailServer, self)._fetch_mails()

        res = self.env['fetchmail.server'].sudo().\
                        with_context(tz=self.env.user.tz).\
                        search([('state', '=', 'done'),
                                ('user', '=', self.env.user.login)])
        if res:
            res[0].run_time = self._run_time()


class FetchMailImmediately(models.AbstractModel):

    _name = 'fetch_mail.imm'

    @api.model
    def get_last_update_time(self):
        res = self.env['fetchmail.server'].sudo()\
                            .with_context(tz=self.env.user.tz)\
                            .search([('state', '=', 'done'),
                                     ('user', '=', self.env.user.login)])
        array = [r.run_time for r in res]
        if array:
            last_update = datetime.datetime.strptime(array[0], \
                                    tools.misc.DEFAULT_SERVER_DATETIME_FORMAT)
            minutes = str(last_update.minute)
            hours = str(last_update.hour)
            if last_update.minute < 10:
                minutes = '0' + str(last_update.minute)
            if last_update.hour < 10:
                hours = '0' + str(last_update.hours)
                return
            return hours + ':' + minutes
        else:
            return None

    @api.model
    def run_fetchmail_manually(self):
        fetchmail_task = self.env.ref('fetchmail.ir_cron_mail_gateway_action')
        fetchmail_model = self.env['fetchmail.server'].sudo()\
                            .with_context(tz=self.env.user.tz)\
                            .search([('state', '=', 'done'),
                                     ('user', '=', self.env.user.login)])
        fetchmail_task._try_lock()
        fetchmail_model.with_context(run_fetchmail_manually=True)._fetch_mails()
