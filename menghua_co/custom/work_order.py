import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class WorkOrder(Document):
    def after_insert(self):
        make_manufacturing_order_auto(self)

@frappe.whitelist()
def make_manufacturing_order_auto(doc):
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

def update_dashboard_link_for_core_doctype(doctype, link_doctype, link_fieldname, group=None):
    try:
        d = frappe.get_doc("Customize Form")
        
        if doctype:
            d.doc_type = doctype
        
        d.run_method("fetch_to_customize")
        
        for link in d.get('links'):
            if link.link_doctype == link_doctype and link.link_fieldname == link_fieldname:
                return
        
        d.append('links', dict(link_doctype=link_doctype, link_fieldname=link_fieldname, table_fieldname=None, group=group))
        d.run_method("save_customization")
        
        frappe.clear_cache()

    except Exception:
        frappe.log_error(frappe.get_traceback())

def after_work_order_creation(doc, method):
    update_dashboard_link_for_core_doctype(
        doctype="Work Order", 
        link_doctype="Manufacturing Order", 
        link_fieldname="work_order", 
        group="Reference"
    )

def after_insert_combined(doc, method):
    make_manufacturing_order_auto(doc)
    after_work_order_creation(doc, method)
