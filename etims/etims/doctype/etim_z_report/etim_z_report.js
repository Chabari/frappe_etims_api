// Copyright (c) 2025, Geetab Technologies Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on("Etim Z-Report", {
	refresh(frm) {

	},
    onload: function (frm) {

		if (frm.doc.docstatus === 0) frm.set_value("period_end_date", frappe.datetime.now_datetime());
	},

    period_start_date (frm) {
		if (frm.doc.period_start_date && frm.doc.period_end_date) {
			reset_values(frm);
			frappe.run_serially([
				() => frm.trigger("get_pos_invoices")
			]);
		}
	},

    get_pos_invoices (frm) {
		frappe.call({
            method: "get_sale_invoices",
            doc: frm.doc,
			callback: (r) => {
				let pos_docs = r.message;
				set_form_data(pos_docs, frm);
				refresh_fields(frm);
			}
		});
	},
});

function set_form_data (data, frm) {
	data.forEach(d => {
		add_to_pos_transaction(d, frm);
		frm.doc.grand_total += flt(d.grand_total);
		frm.doc.net_total += flt(d.net_total);
		frm.doc.total_tax += flt(d.total_taxes_and_charges);
		frm.doc.paid_amount += flt(d.paid_amount);
		if(d.is_return == 1){
			frm.doc.credit_note_count += 1
		}
		add_to_payments(d, frm);
		add_to_taxes(d, frm);
	});
}

function add_to_payments (d, frm) {
	d.payments.forEach(p => {
		const payment = frm.doc.payment_reconciliation.find(pay => pay.mode_of_payment === p.mode_of_payment);
		if (payment) {
			let amount = p.amount;
			let cash_mode_of_payment = 'Cash';
			if (payment.mode_of_payment == cash_mode_of_payment) {
				amount = p.amount - d.change_amount;
			}
			payment.expected_amount += flt(amount);
		} else {
			frm.add_child("payment_reconciliation", {
				mode_of_payment: p.mode_of_payment,
				opening_amount: 0,
				closing_amount: p.amount || 0,
				expected_amount: p.amount || 0
			});
		}
	});
}


function add_to_pos_transaction (d, frm) {
	frm.add_child("linked_invoices", {
		sales_invoice: d.name,
		posting_date: d.posting_date,
		grand_total: d.grand_total,
		customer: d.customer
	});
}

function add_to_taxes (d, frm) {
	d.taxes.forEach(t => {
		const tax = frm.doc.taxes.find(tx => tx.account_head === t.account_head && tx.rate === t.rate);
		if (tax) {
			tax.amount += flt(t.tax_amount);
		} else {
			frm.add_child("taxes", {
				account_head: t.account_head,
				rate: t.rate,
				amount: t.tax_amount
			});
		}
	});
}

function reset_values (frm) {
	frm.set_value("linked_invoices", []);
	frm.set_value("payment_reconciliation", []);
	frm.set_value("taxes", []);
	frm.set_value("grand_total", 0);
	frm.set_value("net_total", 0);
}

function refresh_fields (frm) {
	frm.refresh_field("linked_invoices");
	frm.refresh_field("payment_reconciliation");
	frm.refresh_field("taxes");
	frm.refresh_field("grand_total");
	frm.refresh_field("net_total");
	frm.refresh_field("total_tax");
}
