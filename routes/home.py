from fasthtml import common as c

from components.breadcrumb import breadcrumb
from components.cards import label_card
from components.header import header
from components.sidebar import sidebar_com
from routes.auth import is_token_expired


def home_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        sidebar = c.P()
        return c.RedirectResponse('/logout', status_code=303)

    sidebar = sidebar_com()
    permissions = sess.get("permissions")
    is_superuser = sess.get("is_superuser")
    cashier = c.P(cls="hidden")
    editor = c.P(cls="hidden")

    if is_superuser:
        cashier = label_card("Cashier", url="/cashier")
        editor = label_card("Editor", url="/editor")
    elif "view_city" in permissions:
        cashier = label_card("Cashier", url="/cashier")
    elif "view_country" in permissions:
        editor = label_card("Editor", url="/editor")

    home = c.Title("Home"), c.Div(
        header(sess),
        sidebar,
        c.Div(
            breadcrumb(),
            c.Div(
                c.Div(
                    cashier,
                    editor,
                    cls="flex flex-wrap justify-center gap-4 sm:gap-6 md:gap-10",
                ),
                cls="flex justify-center items-center",
                style="min-height: 82vh"
            ),
            cls="bg-gray-600 font-inter md:ml-64 p-2",
            id="content",
            style="min-height: 94vh"
        ),
    )
    return home

