import frappe
from etims.utils import *

def on_submit(doc, method):
    if doc.custom_send_for_signing == 1 and get_main_company().custom_activate_etims == 1:
        items = []
        for itm in doc.items:
            item = frappe.get_doc("Item", itm.item_code)
            myitem = {
                "itemCode": item.custom_etims_item_code if item.custom_etims_item_code else "",
                "qty": itm.qty,
                "pkg": 0,
                "unitPrice": abs(itm.rate),
                "amount": abs(itm.amount),
                "discountAmount": 0
            }
            items.append(myitem)
        taxid = ""
        if doc.tax_id:
            taxid = doc.tax_id
        payload = {
            "traderInvoiceNo": doc.name,
            "totalAmount": abs(doc.grand_total),
            "paymentType": "02" if doc.status == "Unpaid" else "01",
            "salesTypeCode": "C" if doc.custom_etims_invoice_no else "N",
            "receiptTypeCode": "R" if doc.status == "Return" else "S",
            "salesStatusCode": "01",
            "salesDate": get_datetime(f"{doc.posting_date} {doc.posting_time}"),
            "currency": "KES",
            "exchangeRate": 1.0,
            "salesItems": items,
            "customerPin": taxid
        }
        res = post('/invoices', payload)
        if res and res['status'] == 200:
            doc.custom_etims_invoice_no = str(res['data']['invoiceNo'])
            doc.custom_etims_internal_data = res['data']['internalData']
            doc.custom_etims_signature = res['data']['signature']
            doc.custom_etims_scdc_id = res['data']['scdcId']
            doc.custom_etims_scu_receipt_date = res['data']['scuReceiptDate']
            doc.custom_etims_scu_receipt_no = str(res['data']['scuReceiptNo'])
            doc.custom_etims_invoiceverification_url = res['data']['invoiceVerificationUrl']
            doc.db_update()
        
def on_cancel(doc, method):
    if doc.custom_etims_invoice_no:
        delete(f'/invoices/{doc.custom_etims_invoice_no}')
    
    
@frappe.whitelist(allow_guest=True)
def test_payload(name):
    doc = frappe.get_doc("Sales Invoice", name)
    items = []
    for itm in doc.items:
        item = frappe.get_doc("Item", itm.item_code)
        myitem = {
            "itemCode": item.custom_etims_item_code if item.custom_etims_item_code else "",
            "qty": itm.qty,
            "pkg": 0,
            "unitPrice": abs(itm.rate),
            "amount": abs(itm.amount),
            "discountAmount": 0
        }
        items.append(myitem)
    taxid = ""
    if doc.tax_id:
        taxid = doc.tax_id
    payload = {
        "traderInvoiceNo": doc.name,
        "totalAmount": abs(doc.grand_total),
        "paymentType": "02" if doc.status == "Unpaid" else "01",
        "salesTypeCode": "C" if doc.custom_etims_invoice_no else "N",
        "receiptTypeCode": "R" if doc.status == "Return" else "S",
        "salesStatusCode": "01",
        "salesDate": get_datetime(f"{doc.posting_date} {doc.posting_time}"),
        "currency": "KES",
        "exchangeRate": 1.0,
        "salesItems": items,
        "customerPin": taxid
    }
    res = post('/invoices', payload)
    frappe.response.res = res
    if res and res['status'] == 200:
        doc.custom_etims_invoice_no = str(res['data']['invoiceNo'])
        doc.custom_etims_internal_data = res['data']['internalData']
        doc.custom_etims_signature = res['data']['signature']
        doc.custom_etims_scdc_id = res['data']['scdcId']
        doc.custom_etims_scu_receipt_date = res['data']['scuReceiptDate']
        doc.custom_etims_scu_receipt_no = str(res['data']['scuReceiptNo'])
        doc.custom_etims_invoiceverification_url = res['data']['invoiceVerificationUrl']
        doc.db_update()
        
    frappe.response.doc = doc