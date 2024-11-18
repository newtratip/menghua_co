frappe.listview_settings["Manufacturing Order"] = {
    add_fields: [
        "id",               
        "customer_name",    
        "date",            
        "delivery_date",    
        "status",        
        "item_name",      
        "quantity",         
        "uom"             
    ],
    get_indicator: function (doc) {
        if (!doc.status) {
            doc.status = "ร่าง";
        }

        let indicator = [__(doc.status), frappe.utils.guess_colour(doc.status), "status,=," + doc.status];

        switch (doc.status) {
            case "ร่าง":
                indicator[1] = "orange"; 
                break;
            case "รอผลิต":
                indicator[1] = "yellow"; 
                break;
            case "พิมพ์ปก":
                indicator[1] = "blue"; 
                break;
            case "ระหว่างผลิต":
                indicator[1] = "purple"; 
                break;
            case "ห่อพลาสติก":
                indicator[1] = "pink";
                break;
            case "เข้าคลัง":
                indicator[1] = "green";
                break;
            case "ส่งออก":
                indicator[1] = "red";
                break;
            case "ยกเลิก":
                indicator[1] = "red";
                break;
        }
        
        return indicator; 
    },
};
