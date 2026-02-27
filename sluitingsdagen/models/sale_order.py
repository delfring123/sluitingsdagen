from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import _
class sale_order(models.Model):
	_inherit = "sale.order"

	

	def notAvailableForDelivery(self):
		deliveryDate = self.commitment_date
		if deliveryDate:
			return self.partner_id.isDaySelected(deliveryDate.weekday())
		return False

	
	@api.onchange('commitment_date')
	def _onchange_deliveryDate(self):
		if self.notAvailableForDelivery():
			raise UserError(_("The selected delivery date falls on a closing day. Please select another date."))

	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		print("\n\n\n\n\nPartner changed\n\n\n\n\n")
		if self.notAvailableForDelivery():
			print("\n\n\n\n\nError triggered\n\n\n\n\n")
			raise UserError(_("The selected customer is closed on te selected delivery date. Please select another date and try again."))
		