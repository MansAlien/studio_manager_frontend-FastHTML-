from fasthtml import common as c

from components.breadcrumb import breadcrumb
from routes.auth import is_blacklisted, is_token_expired


def employee_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)
    tabs = [
        {"name": "Settings", "url": "/settings"},
        {"name": "Employee", "url": "#"}
    ]




    employee = c.Div(
        breadcrumb(tabs),
        c.Div(
            cls="row row-cols-1 row-cols-sm-2 row-cols-md-4 g-3",
            id="cards",
            hx_get="/settings/employee/cards",
            hx_swap="innerHTML",
            hx_trigger="load, every 5s",
            hx_target="this"
        ),
        cls="bg-gray-600 font-inter p-2",
        id="content",
        style="min-height: 100vh"
    ),
    return employee
