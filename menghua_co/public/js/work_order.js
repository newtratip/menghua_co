frappe.ui.form.on('Work Order', {
    refresh(frm) {
        frm.page.add_inner_button('Manufacturing Order', function() {
            frm.events.create_manufacturing_order(frm);
        }, 'Create');
    },

    create_manufacturing_order: function (frm) {
        frappe.call({
            method: "menghua_co.custom.work_order.create_manufacturing_order", 
            args: {
                source_name: frm.docname,  
                work_order: frm.docname,   
                skip_auto_mo_check: true   
            }
        });
    }
});
