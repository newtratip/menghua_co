from frappe import _

def get_data():
    return {
        "fieldname": "manufacturing_order", 
        "non_standard_fieldnames": {
            "Stock Entry": "stock_entry_type", 
        },
        "transactions": [
            {"label": _("Reference"), "items": ["Stock Entry"],}, 
        ],
    }
