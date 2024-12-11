frappe.ui.form.on('Purchase Invoice', {
    bill_no: function(frm) {
        if (frm.doc.bill_no) {
            frm.set_value('tax_invoice_number', frm.doc.bill_no);
        }
    },
    bill_date: function(frm) {
        if (frm.doc.bill_date) {
            frm.set_value('tax_invoice_date', frm.doc.bill_date);
        }
    }
});