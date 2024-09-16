from fasthtml import common as c

from components.breadcrumb import breadcrumb
from components.cards import status_card
from routes.auth import is_token_expired


def employee_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    tabs = [
        {"name": "Settings", "url": "/settings"},
        {"name": "Employee", "url": "#"}
    ]


    employee = c.Div(
        breadcrumb(tabs),
        c.Div(
            c.Div(
                status_card("Online", "online", 12),
                status_card("Active", "active", 12),
                status_card("Offline", "offline", 12, "red"),
                status_card("Inactive", "inactive", 12, "red"),
                cls="grid sm:grid-cols-2 md:grid-cols-4 gap-4 mb-4"
            ),
            cls="row row-cols-1 row-cols-sm-2 row-cols-md-4 g-3",
            id="cards"
        ),
        cls="bg-gray-600 font-inter p-2",
        id="content",
        style="min-height: 100vh"
    ),
    return employee
