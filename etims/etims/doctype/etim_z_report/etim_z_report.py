# Copyright (c) 2025, Geetab Technologies Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EtimZReport(Document):
	@frappe.whitelist()
	def get_sale_invoices(self):
		currency = frappe.get_cached_value("Company", self.company, "default_currency")
		data = frappe.db.sql(
        	"""
			select
				name
			from
				`tabSales Invoice`
			where
				docstatus = 1 AND TIMESTAMP(CONCAT(posting_date, ' ', posting_time))
        		BETWEEN %s AND %s
			""",
				(self.period_start_date, self.period_end_date),
				as_dict=1,
		)
		data = [frappe.get_doc("Sales Invoice", d.name).as_dict() for d in data]
		return data
				
