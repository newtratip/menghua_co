// Copyright (c) 2024, Ecosoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('Manufacturing Order', {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {  
            frm.add_custom_button(__('Change Status'), function() {
                let status_options = [
                    { "label": "ร่าง", "value": "ร่าง" },
                    { "label": "พิมพ์ปก", "value": "พิมพ์ปก" },
                    { "label": "ระหว่างผลิต", "value": "ระหว่างผลิต" },
                    { "label": "ห่อพลาสติก", "value": "ห่อพลาสติก" },
                    { "label": "เข้าคลัง", "value": "เข้าคลัง" },
                    { "label": "ส่งออก", "value": "ส่งออก" }
                ];

                let dialog = new frappe.ui.Dialog({
                    title: __('เลือกสถานะใหม่'),
                    fields: [
                        {
                            fieldtype: 'Select',
                            label: __('เลือกสถานะ'),
                            fieldname: 'new_status',
                            options: status_options.map(function(option) { return option.value; }),
                            reqd: 1
                        }
                    ],
                    primary_action_label: __('ยืนยัน'),
                    primary_action: function() {
                        let selected_status = dialog.get_value('new_status');
                        frm.set_value('status', selected_status); 
                        frm.refresh_field('status'); 
                        frm.save();
                        dialog.hide(); 
                    }
                });

                dialog.show(); 
            });
        }
    }
});
