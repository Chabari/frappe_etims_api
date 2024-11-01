# Copyright (c) 2024, Geoffrey Karani and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils.nestedset import get_descendants_of


def execute(filters=None):
	filters = frappe._dict(filters or {})
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date cannot be greater than To Date"))

	columns = get_columns()
	data = get_items(filters)
	return columns, data

def get_columns():
	return [
		
  		{
				"label": _("Invoice"),
				"fieldname": "invoice",
				"fieldtype": "Link",
				"options": "Sales Invoice",
				"width": 120,
			},
		{
			"label": _("Customer"),
			"fieldtype": "Link",
			"fieldname": "customer",
			"options": "Customer",
			"width": 180,
		},
		{"label": _("Invoice Date"), "fieldtype": "Date", "fieldname": "posting_date", "width": 150},
		{"label": _("POS Shift"), "fieldtype": "Data", "fieldname": "posa_pos_opening_shift", "width": 200},
		{"label": _("Grand Total"), "fieldtype": "Float", "fieldname": "grand_total", "width": 150},
		{"label": _("Net Total"), "fieldtype": "Float", "fieldname": "net_total", "width": 150},
		{"label": _("Total Taxes"), "fieldtype": "Float", "fieldname": "total_taxes_and_charges", "width": 150},
		{"label": _("Etims Invoice Number"), "fieldtype": "Data", "fieldname": "custom_etims_invoice_no", "width": 200},
		{"label": _("SCU Receipt Number"), "fieldtype": "Data", "fieldname": "custom_etims_scu_receipt_no", "width": 200},
	]

def get_items(filters):
	data = []

	sales_invoice_records = get_sales_data(filters)

	for record in sales_invoice_records:
		row = {
			"invoice": record.get('name'),
			"customer": record.get("customer"),
			"posting_date": record.get("posting_date"),
			"posa_pos_opening_shift": record.get("posa_pos_opening_shift"),
			"grand_total": record.get("grand_total"),
			"net_total": record.get("net_total"),
			"total_taxes_and_charges": record.get("total_taxes_and_charges"),
			"custom_etims_invoice_no": record.get("custom_etims_invoice_no"),
			"custom_etims_scu_receipt_no": record.get("custom_etims_scu_receipt_no")
		}
		data.append(row)

	return data


def get_sales_data(filters):
	db_so = frappe.qb.DocType("Sales Invoice")

	query = (
		frappe.qb.from_(db_so)
		.select(
			db_so.name,
			db_so.customer,
			db_so.posting_date,
			db_so.territory,
			db_so.project,
			db_so.company,
			db_so.posa_pos_opening_shift,
			db_so.grand_total,
			db_so.net_total,
			db_so.total_taxes_and_charges,
			db_so.custom_etims_invoice_no,
			db_so.custom_etims_scu_receipt_no,
		)
		.where(db_so.docstatus == 1)
		.where(db_so.is_return == 0)
	)

	if filters.get("from_date"):
		query = query.where(db_so.posting_date >= filters.from_date)

	if filters.get("to_date"):
		query = query.where(db_so.posting_date <= filters.to_date)

	if filters.get("filter_by"):
		if filters.get("filter_by") == "Not Signed":
			query = query.where(db_so.custom_etims_scu_receipt_no.isnull())
		else:
			query = query.where(db_so.custom_etims_scu_receipt_no.isnotnull())

	if filters.get("customer"):
		query = query.where(db_so.customer == filters.customer)

	return query.run(as_dict=1)



