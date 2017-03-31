odoo.define('mail_check_immediately.mail_check', function(require){
"use strict";
var $ = require('$');
var core = require('web.core');
var Model = require('web.Model');
var ControlPanel = require('web.ControlPanel');


ControlPanel.include({
   events: {
        "click #fetch_mail_immediately": function (event) {
            this.run_fetchmail_manually();
        },
        "click .oe_fetch_new_mails": function (event) {
            this.run_fetchmail_manually();
        },
   },

    init: function(parent, template) {
        this._super.apply(this, arguments);

        var _this = this;
        this.imm_model = new Model('fetch_mail.imm');
    },

    start: function() {
        var _this = this;
        var res = this._super();
        this.get_last_fetched_time();

        this.get_time_loop = setInterval(function(){
            _this.get_last_fetched_time();
        }, 30000);
        return res;
    },

    run_fetchmail_manually: function(){
        var _this = this;
        this.imm_model.call('run_fetchmail_manually', []).then(function(){
            _this.get_last_fetched_time();
        });
    },

    get_last_fetched_time: function(){
        var _this = this;
        this.imm_model.call('get_last_update_time',[]).then(function(res){
            var value;
            if (res)
                value = $.timeago(res);
            value = value || 'undefined';

            _this.$el.find('span.oe_view_manager_fetch_mail_imm_field').html(value);

        });
    },
});
});
