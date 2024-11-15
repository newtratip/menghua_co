import frappe
from frappe import _

@frappe.whitelist()
def make_manufacturing_order(source_name, target_doc=None):
    from frappe.model.mapper import get_mapped_doc

    def set_missing_values(source, target):
        target.date = source.transaction_date  
        target.delivery_date = source.delivery_date
        target.company = source.company

        for item in source.items:
            target.append('items', {
                'item_code': item.item_code,
                'item_name': item.item_name,
                'quantity': item.qty,
                'uom': item.uom,
            })

    doclist = get_mapped_doc(
        "Sales Order", 
        source_name, 
        {
            "Sales Order": {  
                "doctype": "Manufacturing Order", 
            }
        },
        target_doc, 
        set_missing_values, 
    )

    return doclist

