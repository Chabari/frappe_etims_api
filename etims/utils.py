import frappe
import requests
from erpnext import get_default_company
from datetime import datetime
from base64 import b64encode
from io import BytesIO

from requests.auth import HTTPBasicAuth

import qrcode

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_main_company():
    return frappe.get_doc("Company", get_default_company())

def etims_main_url():
    return get_main_company().custom_etims_production_url

def etims_password():
    return get_main_company().custom_etims_password

def etims_username():
    return get_main_company().custom_etims_username

def get(endpoint):
    response = requests.get(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=headers)
    if not response.ok:
        return False
    return response.json()

def delete(endpoint):
    response = requests.delete(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=headers)
    if not response.ok:
        return False
    return response.json()

def post(endpoint, payload):
    response = requests.post(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=headers, json=payload)
    if not response.ok:
        return False
    return response.json()

def put(endpoint, payload):
    response = requests.put(f'{etims_main_url()}{endpoint}', auth=HTTPBasicAuth(etims_username(), etims_password()), headers=headers, data=payload)
    if not response.ok:
        return False
    return response.json()

def get_item_type(ty):
    return ty.split('-')[0]

def get_tax_code(ty):
    return ty.split('-')[0]

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

item_groups = [
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "Rodenticide",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "Pumps",
        "hs_code": ""
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "STICKERS\\SPREADER",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "Pumps",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DISINFECTANTS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "STICKERS\\SPREADER",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DISINFECTANTS",
        "hs_code": ""
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DISINFECTANTS",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "DISINFECTANTS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DISINFECTANTS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "DISINFECTANTS",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DISINFECTANTS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "FEEDS",
        "hs_code": "0043.11.00"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "BIO STIMULANTS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "Rodenticide",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "Rodenticide",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "ACARICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FERTILIZERS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "Rodenticide",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "Pumps",
        "hs_code": ""
    },
    {
        "item_group": "STICKERS\\SPREADER",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "STICKERS\\SPREAD",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": "0111.11.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "DEWORMERS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "MINERALS",
        "hs_code": "0039.11.26"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INSECTICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "MISC",
        "hs_code": ""
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "INJECTABLES",
        "hs_code": "0039.11.37"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "HERBICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "SEEDS",
        "hs_code": ""
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FUNGICIDES",
        "hs_code": "0019.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    },
    {
        "item_group": "FOLIARS",
        "hs_code": "0024.12.00"
    }
]