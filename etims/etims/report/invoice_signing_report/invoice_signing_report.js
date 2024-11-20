// Copyright (c) 2024, Geetab Technologies Limited and contributors
// For license information, please see license.txt

frappe.query_reports["Invoice Signing Report"] = {
	"filters": [
		{
			fieldname:"company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company"),
			reqd: 1
		},
		{
			fieldname:"from_date",
			reqd: 1,
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
		},
		{
			fieldname:"to_date",
			reqd: 1,
			default: frappe.datetime.get_today(),
			label: __("To Date"),
			fieldtype: "Date",
		},
		{
			label: __("Customer"),
			fieldtype: "Link",
			fieldname: "customer",
			options: "Customer"
		},
		{
			label: __("Filter By"),
			fieldname: "filter_by",
			fieldtype: "Select",
			default: "Not Signed",
			options: ["Signed Invoices", "Not Signed"]
		}
	],
};
