// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Salary Structure Assignment', {
	setup: function(frm) {
		frm.set_query("customer", function() {
			return {
				query: "erpnext.controllers.queries.customer_query"
			}
		});
		frm.set_query("salary_structure", function() {
			return {
				filters: {
					company: frm.doc.company,
					docstatus: 1,
					is_active: "Yes"
				}
			}
		});
	},
	customer: function(frm) {
		if(frm.doc.customer){
			frappe.call({
				method: "frappe.client.get_value",
				args:{
					doctype: "Customer",
					fieldname: "customer_name",
					filters:{
						name: frm.doc.customer
					}
				},
			});
		}
		else{
			frm.set_value("company", null);
		}
	}
});