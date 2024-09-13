app_name = "etims"
app_title = "Etims"
app_publisher = "Geetab Technologies Limited"
app_description = "Geetab KRA Integration"
app_email = "info@geetabtechnologies.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/etims/css/etims.css"
# app_include_js = "/assets/etims/js/etims.js"

# include js, css files in header of web template
# web_include_css = "/assets/etims/css/etims.css"
# web_include_js = "/assets/etims/js/etims.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "etims/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "etims/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "etims.utils.jinja_methods",
# 	"filters": "etims.utils.jinja_filters"
# }

doc_events = {
    "Item": {
        "after_insert": "etims.api.item.after_insert",
        "on_update": "etims.api.item.on_update",
        "on_trash": "etims.api.item.on_trash",
    },
    "Sales Invoice": {
        "on_submit": "etims.api.invoice.on_submit",
        "on_cancel": "etims.api.invoice.on_cancel",
    }
}

jinja = {
	"methods": [
		"etims.utils.etims_qr_code",
	],
}


fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                (
                    "Company-custom_customizations",
                    "Company-custom_maintain_etims_stock",
                    "Company-custom_etims_password",
                    "Company-custom_etims_username",
                    "Item-custom_etims_item_code",
                    "Item-custom_item_tax_class",
                    "Item-custom_item_tax_type",
                    "Sales Invoice-custom_etims_scu_receipt_no",
                    "Sales Invoice-custom_etims_scdc_id",
                    "Sales Invoice-custom_etims_internal_data",
                    "Sales Invoice-custom_column_break_hbmxi",
                    "Sales Invoice-custom_etims_invoiceverification_url",
                    "Sales Invoice-custom_etims_scu_receipt_date",
                    "Sales Invoice-custom_etims_signature",
                    "Sales Invoice-custom_etims_invoice_no",
                    "Sales Invoice-custom_etims",
                ),
            ]
        ],
    },
    
]


# Installation
# ------------

# before_install = "etims.install.before_install"
# after_install = "etims.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "etims.uninstall.before_uninstall"
# after_uninstall = "etims.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "etims.utils.before_app_install"
# after_app_install = "etims.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "etims.utils.before_app_uninstall"
# after_app_uninstall = "etims.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "etims.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"etims.tasks.all"
# 	],
# 	"daily": [
# 		"etims.tasks.daily"
# 	],
# 	"hourly": [
# 		"etims.tasks.hourly"
# 	],
# 	"weekly": [
# 		"etims.tasks.weekly"
# 	],
# 	"monthly": [
# 		"etims.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "etims.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "etims.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "etims.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["etims.utils.before_request"]
# after_request = ["etims.utils.after_request"]

# Job Events
# ----------
# before_job = ["etims.utils.before_job"]
# after_job = ["etims.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"etims.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

