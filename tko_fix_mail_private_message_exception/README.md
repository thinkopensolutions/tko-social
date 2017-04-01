Fix Mail Private Message Exception
=======

When incoming SMTP server fetch emails and can't find where to deliver the message Odoo raises followig exception, and respective log:

> Routing: posting a message without model should be with a parent_id (private mesage).

Solution
----------

After installation create an alias, or redirect current alias with same name as the incoming server account to a partner.
This module will deliver the messages to that model. make sure you set Aliased Model and Record Thread ID, if you don't set Owner the messages will be delivered by the Administrator.

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

