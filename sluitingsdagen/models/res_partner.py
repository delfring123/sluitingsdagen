from odoo import models, fields

class res_partner(models.Model):
    _inherit = "res.partner"

    monday = fields.Boolean(string="Monday", default=False)
    tuesday = fields.Boolean(string="Tuesday", default=False)
    wednesday = fields.Boolean(string="Wednesday", default=False)
    thursday = fields.Boolean(string="Thursday", default=False)
    friday = fields.Boolean(string="Friday", default=False)
    saturday = fields.Boolean(string="Saturday", default=False)
    sunday = fields.Boolean(string="Sunday", default=False)
    


    def isDaySelected(self, day):
        if day:
            if day == 0:
                return self.monday
            elif day == 1:
                return self.tuesday
            elif day == 2:
                return self.wednesday
            elif day == 3:
                return self.thursday
            elif day == 4:
                return self.friday
            elif day == 5:
                return self.saturday
            elif day == 6:
                return self.sunday
            else:
                return False