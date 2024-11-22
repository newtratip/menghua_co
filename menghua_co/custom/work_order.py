import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class WorkOrder(Document):
    def after_insert(self):
        auto_create_manufacturing_order(self.name)

@frappe.whitelist()
def auto_create_manufacturing_order(doc, method=None):
    auto_mo = frappe.get_cached_value("Company", doc.company, "custom_enable_manufacturing_order_auto")
    if auto_mo:
        create_manufacturing_order(doc.name, show_message=False)

@frappe.whitelist()
def create_manufacturing_order(source_name, target_doc=None, show_message=True): 
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
    doc = get_mapped_doc(
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
    if doc:
        new_doc = doc.insert()  
        if show_message:
            frappe.msgprint(
                _("Manufacturing Order Created: <a href='/app/manufacturing-order/{0}'>{0}</a>").format(new_doc.name),
                alert=True,
                indicator="green"
            )
