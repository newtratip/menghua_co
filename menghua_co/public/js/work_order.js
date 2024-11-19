frappe.ui.form.on('Work Order', {
    refresh(frm) {
        frm.page.add_inner_button('Manufacturing Order', () => frm.events.make_manufacturing_order(frm), 'Create');
    },

    make_manufacturing_order: function(frm) {
        frappe.model.open_mapped_doc({
            method: "menghua_co.custom.work_order.make_manufacturing_order", 
            frm: frm
        });
    }
});