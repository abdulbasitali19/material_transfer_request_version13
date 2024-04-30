# Copyright (c) 2024, abdul basit ali shaik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MaterialTransferRequest(Document):
	def validate(self):
		self.create_material_transfer()
		
	def on_cancel(self):
		self.cancel_material_transfer()


	def cancel_material_issuance(self):
			doc = frappe.get_doc('Stock Entry', self.naming_series)
			if doc.docstatus == 1:
				doc.cancel()
	

	def create_material_transfer(self):
		doc = frappe.new_doc('Material Request')
		doc.material_request_type = "Material Transfer"
		for i in self.item:
			doc.append("items",{
				"item_code":i.get("item_code"),
				"warehouse":self.target_warehouse,
				"qty":i.get("qty"),
				"uom":i.get("uom"),
				# "cost_center":self.branch,
				"schedule_date":self.required_by
			})
		doc.submit()
