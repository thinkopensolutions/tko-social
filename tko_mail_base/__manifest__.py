# -*- coding: utf-8 -*-
# © 2017 TKO <http://tko.tko-br.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Mail Modules',
    'summary': '',
    'description': 'Installs mail related modules that enhance user usability.',
    'author': 'TKO',
    'category': 'Discuss',
    'license': 'AGPL-3',
    'website': 'http://tko.tko-uk.com',
    'version': '10.0.0.0.0',
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': [
                'tko_mail_optional_autofollow',
                'mail_see_recipients',
                'tko_mail_smtp_per_user',
                'mail_recovery',
                'mail_sent',
                'mail_archives',
                'mail_attachment_popup',
                'tko_email_cc_bcc',
                'res_partner_mails_count'
    ],
    'external_dependencies': {
                                'python': [],
                                'bin': [],
                                },
    'init_xml': [],
    'update_xml': [],
    'css': [],
    'demo_xml': [],
    'test': [],
    'data': [
    ],
}
