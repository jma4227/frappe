import frappe

def execute():
    '''
    Deprecate Feedback Trigger and Rating. This feature was not customizable.
    Now can be achieved via custom_ Web Forms
    '''
    frappe.delete_doc('DocType', 'Feedback Trigger')
    frappe.delete_doc('DocType', 'Feedback Rating')
