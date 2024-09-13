import frappe
from etims.utils import *

def after_insert(doc, method):
    payload = {
        "name": doc.customer_name,
        "pin": doc.tax_id or "",
        "phone": ""
    }   
    res = post('/customers', payload)
    # if res and res['status'] == 200:
    #     doc.custom_etims_item_code = res['data']['itemCode']
    #     doc.save()
        
def on_update(doc, method):
    if doc.custom_etims_item_code:
        payload = {
            "name": doc.customer_name,
            "pin": doc.tax_id or "",
            "phone": ""
        }   
        # put(f'/customers/{doc.custom_etims_item_code}', payload)
        
def on_trash(doc, method):
    pass
    # if doc.custom_etims_item_code:
    #     delete(f'/items/{doc.custom_etims_item_code}')