# Copyright (c) 2024, Ecosoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ManufacturingOrder(Document):
    def before_save(self):
        if self.docstatus == 0:
            if self.mh_status == "ยกเลิก":
                self.mh_status = "ร่าง"
            elif self.mh_status != "ร่าง":
               frappe.throw("Invalid MH Status")

    def before_submit(self):
        if self.mh_status == "ร่าง":
            self.mh_status = "รอผลิต"
            
    def on_cancel(self):
        self.mh_status = "ยกเลิก"
        self.db_update()
        
    def before_update_after_submit(self):
        if self.docstatus == 1: 
            if self.mh_status in ["ร่าง","ยกเลิก"]:
                frappe.throw("Invalid MH Status")