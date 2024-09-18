from fasthtml import common as c

from components.breadcrumb import breadcrumb
from routes.auth import is_blacklisted, is_token_expired


def inventory_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)
    tabs = [
        {"name": "Settings", "url": "/settings"},
        {"name": "Inventory", "url": "#"}
    ]


    inventory = c.Div(
        breadcrumb(tabs),
        cls="bg-gray-600 font-inter p-2",
        id="content",
        style="min-height: 100vh"
    ),
    return inventory
