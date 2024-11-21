frappe.ui.form.on('Work Order', {
    refresh(frm) {
        frm.page.add_inner_button('Manufacturing Order', () => frm.events.make_manufacturing_order(frm), 'Create');
    },

    make_manufacturing_order: function (frm) {
        frappe.call({
            method: "menghua_co.custom.work_order.make_manufacturing_order", 
            args: {
                work_order: frm.docname, 
                manual_trigger: true, 
            },
            freeze: true,
            callback: function (r) {
                if (r.message && r.message.length > 0) {
                    frappe.msgprint({
                        message: __("Manufacturing Orders Created: {0}", [
                            r.message
                                .map(function (name) {
                                    return repl(
                                        '<a href="/app/manufacturing-order/%(name)s">%(name)s</a>',
                                        { name: name }
                                    );
                                })
                                .join(", "),
                        ]),
                        indicator: "green",
                    });
                }
            },
        });
    },
});
