import frappe
import requests
from erpnext import get_default_company
from datetime import datetime
from base64 import b64encode
from frappe.utils.background_jobs import enqueue
from io import BytesIO

from requests.auth import HTTPBasicAuth

import qrcode


def get_main_company():
    return frappe.get_doc("Company", get_default_company())

def etims_main_url():
    return get_main_company().custom_etims_production_url

def etims_password():
    return get_main_company().custom_etims_password

def etims_username():
    return get_main_company().custom_etims_username

def get_headers():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        'tin': get_main_company().custom_kra_pin,
        'bhfId': "00",
    }
    return headers
    
def get(endpoint):
    response = requests.get(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=get_headers())
    if not response.ok:
        return False
    return response.json()

def delete(endpoint):
    response = requests.delete(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=get_headers())
    if not response.ok:
        return False
    return response.json()

def post(endpoint, payload):
    response = requests.post(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=get_headers(), json=payload)
    if not response.ok:
        return False
    return response.json()


def post2(endpoint, payload):
    response = requests.post(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=get_headers(), json=payload)
    return response

def put(endpoint, payload):
    response = requests.put(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=get_headers(), json=payload)
    if not response.ok:
        return False
    return response.json()

def get_item_type(ty):
    return ty.split('-')[0]

def get_taxes():
    if get_default_company() == "LEGHORNS LIMITED":
        return ["Kenya Tax - LL", "VAT 16%"]
    
    if get_default_company() == "THOME AGROFARM LTD":
        return ["Kenya Tax - TAL", "VAT 16%"]

    taxes = frappe.get_all(
        "Item Tax Template",
        filters={"company": get_default_company()},
        fields=["name"]
    )
    return [tax.name for tax in taxes]

def get_tax_code(ty):
    item_group = frappe.get_doc("Item Group", ty.item_group)
    taxes = item_group.taxes
    taxcode = "A"
    if taxes:
        tax = taxes[0]
        item_tax_template = tax.item_tax_template
        if item_tax_template in get_taxes():
            taxcode = "B"#16%
        else:
            taxcode = "A"#excempt
    return taxcode 

def get_datetime(data):
    datetime_obj = datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f')
    return datetime_obj.strftime('%Y%m%d%H%M%S')

def bytes_to_base64_string(data: bytes) -> str:
	"""Convert bytes to a base64 encoded string."""
	return b64encode(data).decode("utf-8")

def add_file_info(data: str) -> str:
	"""Add info about the file type and encoding.
	This is required so the browser can make sense of the data."""
	return f"data:image/png;base64, {data}"

def etims_qr_code(data: str) -> str:
    qr_code_bytes = get_qr_code_bytes(data, format="PNG")
    base_64_string = bytes_to_base64_string(qr_code_bytes)
    return add_file_info(base_64_string)

def get_qr_code_bytes(data, format: str) -> bytes:
	"""Create a QR code and return the bytes."""
	img = qrcode.make(data)
	buffered = BytesIO()
	img.save(buffered, format=format)
	return buffered.getvalue()

def get_delivery_note(name):
    sales_invoice = frappe.get_doc("Sales Invoice", name)
    sales_order_name = None
    for dn in sales_invoice.items:
        if dn.so_detail:
            sales_order_name = dn.so_detail
            break
    if sales_order_name:
        _delivery_note_item = frappe.db.get_value('Delivery Note Item', {'so_detail': sales_order_name}, ['name'], as_dict=1) 
        if _delivery_note_item:
            delivery_note = frappe.get_doc("Delivery Note Item", _delivery_note_item.name)
            return delivery_note.parent
        
    return "N/A"
          
@frappe.whitelist()
def check_the_shift(user):
    
    open_vouchers = frappe.db.get_all(
        "POS Opening Shift",
        filters={
            "user": user,
            "pos_closing_shift": ["in", ["", None]],
            "docstatus": 1,
            "status": "Open",
            "creation" : [ "<", frappe.utils.today() ]
        },
        fields=["name", "pos_profile"],
        order_by="period_start_date desc",
    )
    data = {}
    if len(open_vouchers) > 0:
        
        data["isOpen"] = True
    else:
        data["isOpen"] = False
    return data

def get_item_payloan(doc):
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
        "stock": 100000 
            if get_main_company().custom_maintain_etims_stock == 0
            else doc.opening_stock 
            if doc.opening_stock 
            else 0
    }   
    
    return payload

@frappe.whitelist(allow_guest=True)  
def update_items():
    items = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE custom_etims_item_code IS NOT NULL
    """)
    for itm in items:
        enqueue(
            method=submit_in_background,
            queue="long",
            is_async=True,
            kwargs={
                "itm": itm,
            },
        )
        
def submit_in_background(kwargs):
    doc = frappe.get_doc('Item', kwargs.get('itm'))
    payload = get_item_payloan(doc)
    put(f'/items/{doc.custom_etims_item_code}', payload)
    