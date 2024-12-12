// Copyright (c) 2024, Ecosoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('Manufacturing Order', {
    customer: function(frm) {
        frm.set_query('sales_order', function() {
            return {
                filters: {
                    'customer': frm.doc.customer
                }
            };
        });
    }
});

frappe.ui.form.on('Manufacturing Order', {
    onload: function(frm) {
        if (frm.doc.docstatus == 0 && frm.doc.mh_status == "ยกเลิก") {
            frm.set_value('mh_status', 'ร่าง');
        }
    },
    
    validate: function(frm) {
        if (frm.doc.docstatus == 0 && frm.doc.mh_status == "ยกเลิก") {
            frm.set_value('mh_status', 'ร่าง');
        }
    }
});