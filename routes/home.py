from fasthtml import common as c

from components.breadcrumb import breadcrumb
from components.header import header
from components.sidebar import sidebar_com
from routes.auth import is_token_expired


def card(label, url="#"):
    return c.Div(
        c.A(
            label,
            href=url,
            cls="w-full h-full flex justify-center items-center"
        ),
        cls="""flex justify-center items-center bg-gray-800 text-white text-2xl font-bold
                rounded-lg p-4 hover:bg-gray-700 hover:scale-105 hover:shadow-lg hover:rotate-1
                transition duration-300 transform shadow-md hover:text-yellow-300 
                hover:-translate-y-1 hover:text-shadow 
                w-full sm:w-64 md:w-80 lg:w-96
                h-40 sm:h-48 md:h-56 lg:h-64""",
    )

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
        cashier = card("Cashier", url="/cashier")
        editor = card("Editor", url="/editor")
    elif "view_city" in permissions:
        cashier = card("Cashier", url="/cashier")
    elif "view_country" in permissions:
        editor = card("Editor", url="/editor")

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
            cls="bg-gray-600 font-inter md:ml-64",
            id="content",
            style="min-height: 94vh"
        ),
    )
    return home

