from fasthtml import common as c

from components.breadcrumb import breadcrumb
from routes.auth import is_token_expired


def inventory_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    tabs = [
        {"name": "Settings", "url": "/settings"},
        {"name": "Inventory", "url": "#"}
    ]


    inventory = c.Div(
            breadcrumb(tabs),
            cls="bg-gray-600 font-inter",
            id="content",
            style="min-height: 94vh"
        ),
    return inventory
