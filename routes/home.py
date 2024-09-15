from fasthtml import common as c

from components.breadcrumb import breadcrumb
from components.header import header
from components.sidebar import sidebar_com
from routes.auth import is_token_expired


# Define card component with responsive classes
def card(label, hx_get=None, hx_target=None, hx_swap=None):
    return c.Div(
        c.A(
            label,
            hx_get=hx_get,
            hx_target=hx_target,
            hx_swap=hx_swap,
            cls="w-full h-full flex justify-center items-center"
        ),
        cls="""flex justify-center items-center bg-gray-800 text-white text-2xl font-bold
                rounded-lg p-4 hover:bg-gray-700 hover:scale-105 hover:shadow-lg hover:rotate-1
                transition duration-300 transform shadow-md hover:text-yellow-300 
                hover:-translate-y-1 hover:text-shadow 
                w-full sm:w-64 md:w-80 lg:w-96
                h-40 sm:h-48 md:h-56 lg:h-64""",  # Adjust width/height based on screen size
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

    # Responsive cards depending on user role
    if is_superuser:
        editor = card("Editor", hx_get="/editor", hx_target="#content", hx_swap="innerHTML")
        cashier = card("Cashier", hx_get="/cashier", hx_target="#content", hx_swap="innerHTML")
    elif "view_city" in permissions:
        cashier = card("Cashier", hx_get="/cashier", hx_target="#content", hx_swap="innerHTML")
    elif "view_country" in permissions:
        editor = card("Editor", hx_get="/editor", hx_target="#content", hx_swap="innerHTML")

    home = c.Title("Studio Vision"), c.Div(
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
                style="min-height: 82vh"  # Ensure full height responsiveness
            ),
            cls="bg-gray-600 font-inter md:ml-64",
            id="content",
            style="min-height: 94vh"
        ),
    )
    return home

