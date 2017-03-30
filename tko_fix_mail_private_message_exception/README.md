tko_fix_mail_private_message_exception
=======

Issue Description
----------


When Imap Server is called and email_from field is not set with your account.alias but the email is in your email server, Odoo generates the following issue:

**Routing: posting a message without model should be with a parent_id (private mesage).**


[...] **CORRECT SET TAKEN FROM LOG**

author_id: [None]
model: [res.partner]
thread_id: [3407]
alias: [mail.alias(290,)]

[...]


[...] **INCORRECT SET TAKEN FROM LOG**

author_id: [None]
model: [False]
thread_id: [False]
alias: [None]

[...]

Solution
----------

When Imap Server is called for account.alias, and email_from is not set on your email correctly, this module overides email_from with your account.alias for you to receive the email.


Credits
=======


Contributors
------------

* Alexandre Rüffer <alexandre.ruffer@tkobr.com>
* Carlos Almeida <carlos.almeida@tkobr.com>

Maintainer
----------

![TKO](https://tkobr.tkobr.com/website/image/ir.attachment/50170_af65c50/datas)

https://tkobr.tkobr.com/

This module is maintained by the ThinkOpen Solutions.

To contribute to this module, please visit:
https://github.com/thinkopensolutions/tko-crm

