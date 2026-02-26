from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class sale_order(models.Model):
	_inherit = "sale.order"

	

	def availableForDelivery(self):
		deliveryDate = self.commitment_date
		if deliveryDate:
			return self.partner_id.isDaySelected(deliveryDate.weekday())
		return False

	@api.onchange('partner_id')
	@api.onchange('commitment_date')
	def _onchange_deliveryDate(self):
		if self.availableForDelivery():
			raise UserError("The selected delivery date falls on a closing day. Please select another date.")
		