# Copyright (c) 2024, Ecosoft and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ManufacturingOrder(Document):
    def before_submit(self):
        if self.status == "ร่าง":
            self.status = "พิมพ์ปก"  
