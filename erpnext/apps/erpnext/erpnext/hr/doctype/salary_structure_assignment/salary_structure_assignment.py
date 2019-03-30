
# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate
from frappe.model.document import Document

class DuplicateAssignment(frappe.ValidationError): pass

class SalaryStructureAssignment(Document):
	def customer_value(self):
		customer = frappe.db.get_value("Customer", self.customer)
def get_assigned_salary_structure(customer,on_date,designation):
			if not customer or not on_date:
				return None
				salary_structure = frappe.db.sql("""
					select salary_structure from `tabSalary Structure Assignment`
					where customer=%(customer)s and disgnation = %(designation)s
					and docstatus = 1
					and %(on_date)s >= from_date order by from_date desc limit 1""", {
					'customer': customer,
					'designation':designation,
					'on_date': on_date,
					})
				return salary_structure[0][0] if salary_structure else None