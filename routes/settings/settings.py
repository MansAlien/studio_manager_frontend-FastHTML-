from fasthtml import common as c

from components.header import header
from components.sidebar import list_item, sidebar_com
from routes.auth import is_blacklisted, is_token_expired


def settings_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        sidebar = c.P()
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)
    employee = list_item("Employee", "#", "dynamic", hx_get="/settings/employee", hx_target="#content", hx_swap="innerHTML"),
    inventory = list_item("Inventory", "#", "dynamic", hx_get="/settings/inventory", hx_target="#content", hx_swap="innerHTML"),
    orders = list_item("Orders", "#", "dynamic", hx_get="/settings/orders", hx_target="#content", hx_swap="innerHTML"),
    items = [employee, inventory, orders]
    sidebar = sidebar_com(items)

    settings = c.Title("Settings"), c.Div(
        header(sess),
        sidebar,
        c.Div(
            cls="bg-gray-600 font-inter md:ml-64",
            id="content",
            style="min-height: 94vh",
            hx_get="/settings/employee",
            hx_swap="innerHTML",
            hx_trigger="load",
            hx_target="this"
        ),
    )
    return settings
