import frappe
from etims.utils import *
import json

def after_insert(doc, method):
    if get_main_company().custom_activate_etims == 1:
        payload = get_item_payloan(doc)
        res = post('/items', payload)
        if res and res['status'] == 200:
            doc.custom_etims_item_code = res['data']['itemCode']
            doc.save(ignore_permissions = True)
            frappe.db.commit()
        
def on_update(doc, method):
    if doc.custom_etims_item_code:
        payload = get_item_payloan(doc)
        put(f'/items/{doc.custom_etims_item_code}', payload)
        
def on_trash(doc, method):
    if doc.custom_etims_item_code:
        delete(f'/items/{doc.custom_etims_item_code}')
      
@frappe.whitelist(allow_guest=True)  
def sync_items():
    items = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE custom_etims_item_code IS NULL
    """)
    
    frappe.enqueue('etims.api.item.save_sync_item', queue='long', items=items)
    return "Success"
    
   
def save_sync_item(items):
    try:
        for itm in items:
            doc = frappe.get_doc('Item', itm)
            taxcode = get_tax_code(doc)
            if taxcode == 'B':
                print("tax B")
            
            payload = get_item_payloan(doc)
            res = post('/items', payload)
            if res and res['status'] == 200:
                doc.custom_etims_item_code = res['data']['itemCode']
                doc.save(ignore_permissions = True)
                frappe.db.commit()
            else:
                print("tax A")
    except Exception as e:
        print(str(e))
        frappe.log_error(frappe.get_traceback(), str(e))
        

@frappe.whitelist(allow_guest=True)  
def reset_items():
    items = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
    """)
    for itm in items:
        frappe.db.sql("""
            UPDATE `tabItem` 
            SET custom_etims_item_code = NULL 
            WHERE name = %(item_name)s
        """, {"item_name": itm})
        frappe.db.commit()
        
    return "successfully reset items"

@frappe.whitelist(allow_guest=True)  
def sync_item(name):

    doc = frappe.get_doc('Item', name)
    taxcode = get_tax_code(doc)
    
    payload = get_item_payloan(doc)
    res = post2('/items', payload)
    if not res.ok:
        frappe.response.res = res.json()
        return res
    xres = res.json()

    if xres and xres['status'] == 200:
        doc.custom_etims_item_code = xres['data']['itemCode']
        doc.save(ignore_permissions = True)
        frappe.db.commit()
   
    frappe.response.xres = xres
    
    
@frappe.whitelist(allow_guest=True)  
def get_items():
    items = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE custom_etims_item_code IS NOT NULL
    """)
    all_items = []
    for itm in items:
        doc = frappe.get_doc('Item', itm)
        payload = get_item_payloan(doc)
        response = put(f'/items/{doc.custom_etims_item_code}', payload)
        all_items.append({
            'payload': payload,
            'response': response
        })
        
    # frappe.response.total = len(all_items)
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
    saved = []
    theitems = items['data']
    all_items = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE custom_etims_item_code IS NULL
    """)
    for itm in all_items:
        the_itm = [
            num 
            for num in theitems 
            if num['name'] == itm
        ]
        if len(the_itm) > 0: 
            saved.append(the_itm)
        # xitem = frappe.db.get_value('Item', {'item_name': itm['name']}, ['name'], as_dict=1)
        # if xitem: 
        #     item = frappe.get_doc("Item", xitem.name)
        #     if not item.custom_etims_item_code:
        #         item.custom_etims_item_code = itm['itemCode']
        #         item.save(ignore_permissions = True)
        #         frappe.db.commit()
        #         saved.append(xitem)
            
    frappe.response.saved = saved 
    frappe.response.allitems = theitems 