import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class WorkOrder(Document):
    def after_insert(self):
        make_manufacturing_order(self)

@frappe.whitelist()
def make_manufacturing_order(work_order, manual_trigger=False):

    doc = frappe.get_doc("Work Order", work_order)
    auto_mo = True if manual_trigger else frappe.get_cached_value(
        "Company", doc.company, "custom_enable_manufacturing_order_auto"
    )

    mo_names = []

    if auto_mo:
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

        mapped_doc = get_mapped_doc(
            "Work Order",
            doc.name,
            target_doc,
            None,
            set_missing_values
        )

        if mapped_doc:
            mapped_doc.insert()
            mo_names.append(mapped_doc.name)

    return mo_names