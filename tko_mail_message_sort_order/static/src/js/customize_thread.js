odoo.define('tko_mail_message_sort_order.customize_thread', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');
var ChatThread = require('mail.ChatThread');
var QWeb = core.qweb;
var _t = core._t;

var ORDER = {
    ASC: -1,
    DESC: 1,
};

	ChatThread.include({
	className: 'o_mail_thread',
	
	init: function (parent, options) {
        this._super.apply(this, arguments);
        this.options = _.defaults(options || {}, {
            display_order: ORDER.DESC,
            display_needactions: true,
            display_stars: true,
            display_document_link: true,
            display_avatar: true,
            shorten_messages: true,
            squash_close_messages: true,
            display_reply_icon: false,
        });
        this.expanded_msg_ids = [];
        this.selected_id = null;
    },

    render: function (messages, options) {
        clearTimeout(this.auto_render_timeout);
        var self = this;
        var msgs = _.map(messages, this._preprocess_message.bind(this));
        if (this.options.display_order === ORDER.DESC) {
            msgs.reverse();
        }
        options = _.extend({}, this.options, options);

        // Hide avatar and info of a message if that message and the previous
        // one are both comments wrote by the same author at the same minute
        // and in the same document (users can now post message in documents
        // directly from a channel that follows it)
        var prev_msg;
        _.each(msgs, function (msg) {
            if (!prev_msg || (Math.abs(msg.date.diff(prev_msg.date)) > 60000) ||
                prev_msg.message_type !== 'comment' || msg.message_type !== 'comment' ||
                (prev_msg.author_id[0] !== msg.author_id[0]) || prev_msg.model !== msg.model ||
                prev_msg.res_id !== msg.res_id) {
                msg.display_author = true;
            } else {
                msg.display_author = !options.squash_close_messages;
            }
            prev_msg = msg;
        });

        this.$el.html(QWeb.render('mail.ChatThread', {
            messages: msgs,
            options: options,
            ORDER: ORDER,
        }));

        this.auto_render_timeout = setTimeout(function () {
            if (!self.isDestroyed()) {
                self.render(messages, options);
            }
        }, 1000*60); // re-render the thread every minute to update dates
    },


	});

return ChatThread;

});
