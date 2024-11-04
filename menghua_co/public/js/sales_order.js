frappe.ui.form.on("Sales Order", {
    refresh(frm) {
        if (frm.fields_dict["items"].grid.get_field("item_code")) {
            frm.set_query("item_code", "items", function (doc, cdt, cdn) {
                return {
                    filters: {
                        'custom_allow_standard_type': frm.doc.custom_mh_order_type === "หน้าร้าน" ? 1 : 0,
                        'custom_allow_custom_type': frm.doc.custom_mh_order_type === "สั่งทำ" ? 1 : 0,
                    }
                };
            });
        }
    },
    custom_mh_order_type: function(frm) {
        frm.refresh_field("items");
    }
});
