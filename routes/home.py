from fasthtml import common as c
from components.header import Header
from components.sidebar import sidebar
from components.breadcrumb import breadcrumb
from routes.auth import is_token_expired


def home_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        Sidebar = c.P()
        return c.RedirectResponse('/logout', status_code=303)
    Sidebar = sidebar()

    home =  c.Title("Studio Vision"), c.Div(
        Header(sess),
        Sidebar,
        c.Div(
            breadcrumb(),

            cls="bg-gray-600 font-inter md:ml-64",
            id="content",
            style="height: 94dvh"
        ),
    ) 
    return home
