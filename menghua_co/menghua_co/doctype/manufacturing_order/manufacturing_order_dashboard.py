from frappe import _

def get_data():
    return {
        "fieldname": "manufacturing_order", 
        "internal_and_external_links": {
			"Sales Order": "sales_order",
            "Work Order": "work_order",
		},
        "transactions": [
            {"label": _("Reference"), "items": ["Sales Order", "Work Order"],}, 
        ],
    }
