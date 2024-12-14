import frappe
from erpnext.selling.doctype.quotation.quotation import make_sales_order as old_make_sales_order


@frappe.whitelist()
def make_sales_order(source_name: str, target_doc=None):
    sale_order = old_make_sales_order(source_name, target_doc)
    quotation = frappe.get_doc("Quotation", source_name)
    # Update fields on sales order doctype
    sale_order.delivery_date = quotation.custom_delivery_date
    for item in sale_order.items:
        item.delivery_date = sale_order.delivery_date
    return sale_order
