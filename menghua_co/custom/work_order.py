import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class WorkOrder(Document):
    def after_insert(self):
        make_manufacturing_order_auto(self.name)

@frappe.whitelist()
def make_manufacturing_order_auto(doc, method):
    make_manufacturing_order_auto = frappe.get_cached_value(
        "Company", doc.company, "custom_enable_manufacturing_order_auto"
    )
    if make_manufacturing_order_auto:
        def set_missing_values(source, target):
            target.date = source.creation
            target.company = source.company
            target.sales_order = source.sales_order
            target.item_code = source.production_item
            target.item_name = source.item_name
            target.quantity = source.qty
            target.uom = source.stock_uom

            if source.sales_order:
                sales_order = frappe.get_doc("Sales Order", source.sales_order)
                target.customer = sales_order.customer
                target.delivery_date = sales_order.delivery_date

        target_doc = {
            "Work Order": {
                "doctype": "Manufacturing Order",  
            }
        }

        if not target_doc:
            frappe.throw(_("Invalid target_doc for get_mapped_doc"))

        doclist = get_mapped_doc(
            "Work Order",  
            doc.name,  
            target_doc,  
            None,  
            set_missing_values 
        )

        if doclist:
            doclist.insert()  
            frappe.db.commit()  

@frappe.whitelist()
def make_manufacturing_order(source_name, target_doc=None):
    from frappe.model.mapper import get_mapped_doc

    def set_missing_values(source, target):
        target.date = source.creation
        target.company = source.company
        target.sales_order = source.sales_order
        target.item_code = source.production_item
        target.item_name = source.item_name
        target.quantity = source.qty
        target.uom = source.stock_uom

        if source.sales_order:
            sales_order = frappe.get_doc("Sales Order", source.sales_order)
            target.customer = sales_order.customer  
            target.delivery_date = sales_order.delivery_date

    doclist = get_mapped_doc(
        "Work Order", 
        source_name, 
        {
            "Work Order": {  
                "doctype": "Manufacturing Order", 
            }
        },
        target_doc, 
        set_missing_values, 
    )

    return doclist
