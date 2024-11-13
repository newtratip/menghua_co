frappe.listview_settings["Manufacturing Order"] = {
    add_fields: [
        "customer_name",
        "status",
        "date",
    ],
    get_indicator: function (doc) {
        if (doc.status === "ร่าง") {
            return [__("ร่าง"), "orange", "status,=,ร่าง"];
        } else if (doc.status === "พิมพ์ปก") {
            return [__("พิมพ์ปก"), "blue", "status,=,พิมพ์ปก"];
        } else if (doc.status === "ระหว่างผลิต") {
            return [__("ระหว่างผลิต"), "purple", "status,=,ระหว่างผลิต"];
        } else if (doc.status === "ห่อพลาสติก") {
            return [__("ห่อพลาสติก"), "pink", "status,=,ห่อพลาสติก"];
        } else if (doc.status === "เข้าคลัง") {
            return [__("เข้าคลัง"), "green", "status,=,เข้าคลัง"];
        } else if (doc.status === "ส่งออก") {
            return [__("ส่งออก"), "red", "status,=,ส่งออก"];
        }
    },
    onload: function (listview) {
        const changeStatus = (status) => {
            const method = "mennghua_co.mennghua_co.doctype.manufacturing_order.manufacturing_order.update_status";
            listview.call_for_selected_items(method, { status: status });
        };

        listview.page.add_menu_item(__("เปลี่ยนสถานะเป็น ร่าง"), function () {
            changeStatus("ร่าง");
        });

        listview.page.add_menu_item(__("เปลี่ยนสถานะเป็น พิมพ์ปก"), function () {
            changeStatus("พิมพ์ปก");
        });

        listview.page.add_menu_item(__("เปลี่ยนสถานะเป็น ระหว่างผลิต"), function () {
            changeStatus("ระหว่างผลิต");
        });

        listview.page.add_menu_item(__("เปลี่ยนสถานะเป็น ห่อพลาสติก"), function () {
            changeStatus("ห่อพลาสติก");
        });

        listview.page.add_menu_item(__("เปลี่ยนสถานะเป็น เข้าคลัง"), function () {
            changeStatus("เข้าคลัง");
        });

        listview.page.add_menu_item(__("เปลี่ยนสถานะเป็น ส่งออก"), function () {
            changeStatus("ส่งออก");
        });
    },
};
