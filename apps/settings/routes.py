from apps.cashier.cashier import cashier_get
from apps.settings.settings.employee.employee import employee_get
from apps.settings.settings.employee.employee_cards import get_employee_cards
from apps.settings.settings.employee.employee_table import get_employee_table
from apps.settings.settings.inventory import inventory_get
from apps.settings.settings.orders import orders_get
from apps.settings.settings.settings import settings_get


def settings_register_routes(app):
    @app.get("/cashier")
    def cashier(sess):
        return cashier_get(sess)

    @app.get("/settings")
    def settings(sess):
        return settings_get(sess)

    @app.get("/settings/employee")
    def employee_settings(sess):
        access_token = sess["access_token"]
        return employee_get(access_token)

    @app.get("/settings/employee/cards")
    def employee_cards(sess):
        return get_employee_cards(sess)

    @app.get("/settings/employee/table")
    def employee_table(sess):
        return get_employee_table(sess)

    @app.get("/settings/inventory")
    def inventory_settings(sess):
        return inventory_get(sess)

    @app.get("/settings/orders")
    def orders_settings(sess):
        return orders_get(sess)
