from odoo import api, models, _
from odoo.exceptions import ValidationError
from validate_email import validate_email

class Users(models.Model):
    _inherit = "res.users"

    @api.model
    def create(self, vals):
        res = super(Users, self).create(vals)
        is_valid = False
        for user in res:
            is_valid = validate_email(str(user.login))
        if is_valid == True:
            return res
        else:
            raise ValidationError(_('Invalid email address!'))

    @api.multi
    def write(self, values):
        res = super(Users, self).write(values)
        is_valid = False
        for user in self:
            is_valid = validate_email(str(user.login))
        if is_valid == True:
            return res
        else:
            raise ValidationError(_('Invalid email address!'))
