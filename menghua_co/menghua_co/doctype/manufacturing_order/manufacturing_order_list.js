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
};
