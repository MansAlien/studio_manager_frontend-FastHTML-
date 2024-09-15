from fasthtml import common as c

from components.breadcrumb import breadcrumb
from components.header import header
from components.sidebar import list_item, sidebar_com
from routes.auth import is_token_expired


def cashier_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        sidebar = c.P()
        return c.RedirectResponse('/logout', status_code=303)
    editor = list_item("Editor", "/editor", "settings"),
    items = [editor]
    sidebar = sidebar_com(items)
    tabs = [
        {"name": "Cashier", "url": "#"}
    ]


    cashier = c.Title("Home"), c.Div(
        header(sess),
        sidebar,
        c.Div(
            breadcrumb(tabs),
            cls="bg-gray-600 font-inter md:ml-64",
            id="content",
            style="min-height: 94vh"
        ),
    )
    return cashier

