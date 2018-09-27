odoo.define('tko_compose_mail.compose_mail', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');
var Widget = require('web.Widget');
var SystrayMenu = require('web.SystrayMenu');
var rpc = require('web.rpc');

var _t = core._t;
var qweb = core.qweb;

var ComposeMailTray = Widget.extend({
    template:'ComposeMailTray',
    events: {
        "click": "on_click",
    },
    on_click: function (event) {
        var context = {'active_model': 'res.partner', 'active_id': session.partner_id}
        return this.do_action({
            type: 'ir.actions.act_window',
            name: "Compose Mail",
            res_model: 'mail.compose.message',
             views:[[false, 'form']],
            view_type: 'form',
            view_mode: 'form',
            target: 'new',
            context: context,
        });
    },
    start_voip_screenshare_call: function (event) {

    },
    start_voip_audio_call: function (event) {

    },
    start_voip_video_call: function (event) {
    },
});

SystrayMenu.Items.push(ComposeMailTray);

});