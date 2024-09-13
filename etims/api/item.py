import frappe
from etims.utils import *

def after_insert(doc, method):
    payload = {
        "name": doc.item_code,
        "orgCountryCode": "KE",
        "unitPrice": doc.standard_rate or 1,
        "itemTypeCode": get_item_type(doc.custom_item_tax_type) 
            if doc.custom_item_tax_type 
            else "2",
        "taxCode": get_tax_code(doc.custom_item_tax_class) 
            if doc.custom_item_tax_class 
            else "A",
        "qtyUnitCode": "U",
        "pkgUnitCode": "CT",
        "itemClassCode": "99012019",
        "initialStock": 100000 
            if get_main_company().custom_maintain_etims_stock == 0
            else doc.opening_stock 
            if doc.opening_stock 
            else 0,
    }   
    # res = post('/items', payload)
    # if res and res['status'] == 200:
    #     doc.custom_etims_item_code = res['data']['itemCode']
    #     doc.save()
        
def on_update(doc, method):
    if doc.custom_etims_item_code:
        payload = {
            "name": doc.item_code,
            "orgCountryCode": "KE",
            "unitPrice": doc.standard_rate or 1,
            "itemTypeCode": get_item_type(doc.custom_item_tax_type) 
                if doc.custom_item_tax_type 
                else "2",
            "taxCode": get_tax_code(doc.custom_item_tax_class) 
                if doc.custom_item_tax_class 
                else "A",
            "qtyUnitCode": "U",
            "pkgUnitCode": "CT",
            "itemClassCode": "99012019",
            "initialStock": 100000 
                if get_main_company().custom_maintain_etims_stock == 0
                else doc.opening_stock 
                if doc.opening_stock 
                else 0,
        }   
        put(f'/items/{doc.custom_etims_item_code}', payload)
        
def on_trash(doc, method):
    if doc.custom_etims_item_code:
        delete(f'/items/{doc.custom_etims_item_code}')
      
@frappe.whitelist(allow_guest=True)  
def sync_items():
    succeeded = []
    failed = []
    items = frappe.get_all("Item", filters={"custom_etims_item_code": None},fields=['name'])
    for itm in items:
        doc = frappe.get_doc('Item', itm.name)
        payload = {
            "name": doc.item_code,
            "orgCountryCode": "KE",
            "unitPrice": doc.standard_rate or 1,
            "itemTypeCode": get_item_type(doc.custom_item_tax_type) 
                if doc.custom_item_tax_type 
                else "2",
            "taxCode": get_tax_code(doc.custom_item_tax_class) 
                if doc.custom_item_tax_class 
                else "A",
            "qtyUnitCode": "U",
            "pkgUnitCode": "CT",
            "itemClassCode": "99012019",
            "initialStock": 100000 
                if get_main_company().custom_maintain_etims_stock == 0
                else doc.opening_stock 
                if doc.opening_stock 
                else 0,
        }   
        res = post('/items', payload)
        if res and res['status'] == 200:
            doc.custom_etims_item_code = res['data']['itemCode']
            doc.save()
            succeeded.append({
                'code': res['data']['itemCode'],
                'item': doc.item_name
            })
        else:
            failed.append({
                'item': doc.item_name
            })
            
    frappe.response.failed = failed
    frappe.response.succeeded = succeeded
            
        