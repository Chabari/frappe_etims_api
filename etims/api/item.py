import frappe
from etims.utils import *
import json

def after_insert(doc, method):
    payload = {
        "name": doc.item_code,
        "orgCountryCode": "KE",
        "unitPrice": doc.standard_rate or 1,
        "itemTypeCode": get_item_type(doc.custom_item_tax_type) 
            if doc.custom_item_tax_type 
            else "2",
        "taxCode": get_tax_code(doc),
        "qtyUnitCode": "U",
        "pkgUnitCode": "CT",
        "itemClassCode": "99012019",
        "initialStock": 100000 
            if get_main_company().custom_maintain_etims_stock == 0
            else doc.opening_stock 
            if doc.opening_stock 
            else 0,
    }   
    if get_main_company().custom_activate_etims == 1:
        res = post('/items', payload)
        if res and res['status'] == 200:
            doc.custom_etims_item_code = res['data']['itemCode']
            doc.save(ignore_permissions = True)
            frappe.db.commit()
        
def on_update(doc, method):
    if doc.custom_etims_item_code:
        payload = {
            "name": doc.item_code,
            "orgCountryCode": "KE",
            "unitPrice": doc.standard_rate or 1,
            "itemTypeCode": get_item_type(doc.custom_item_tax_type) 
                if doc.custom_item_tax_type 
                else "2",
            "taxCode": get_tax_code(doc),
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
    failed = []
    vattax = []
    items = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE custom_etims_item_code IS NULL LIMIT 200
    """)
    for itm in items:
        doc = frappe.get_doc('Item', itm)
        taxcode = get_tax_code(doc)
        if taxcode == 'B':
            vattax.append(doc.name)
        payload = {
            "name": doc.item_code,
            "orgCountryCode": "KE",
            "unitPrice": doc.standard_rate or 1,
            "itemTypeCode": get_item_type(doc.custom_item_tax_type) 
                if doc.custom_item_tax_type 
                else "2",
            "taxCode": taxcode,
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
            doc.save(ignore_permissions = True)
            frappe.db.commit()
        else:
            failed.append({
                'item': doc.item_name,
                'res': res
            })
            
    frappe.response.failed = failed
    frappe.response.vattax = vattax
    
@frappe.whitelist(allow_guest=True)  
def get_items():
    items = []
    all_items = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE custom_etims_item_code IS NULL
    """)
    # for itm in all_items:
    #     item = frappe.get_doc("Item", itm)
    #     item.custom_etims_item_code = None
    #     item.save(ignore_permissions = True)
    #     frappe.db.commit()
    #     items.append(item)
        
    frappe.response.items = all_items
        
   
@frappe.whitelist(allow_guest=True)  
def update_item_code(name, code):

    item = frappe.get_doc("Item", name)
    item.custom_etims_item_code = code
    item.save(ignore_permissions = True)
    frappe.db.commit()
    frappe.response.items = item
        
@frappe.whitelist(allow_guest=True)  
def allign_items():
    items = get('/items')
    theitems = json.loads(items)
    saved = []
    frappe.response.items = theitems
    for itm in theitems:
        item = frappe.get_doc("Item", itm.get('name'))
        if not item.custom_etims_item_code:
            item.custom_etims_item_code = itm.get('itemCode')
            item.save(ignore_permissions = True)
            frappe.db.commit()
            saved.append(item)
            
    frappe.response.saved = saved 