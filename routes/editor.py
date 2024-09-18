from fasthtml import common as c

from components.breadcrumb import breadcrumb
from components.header import header
from components.sidebar import list_item, sidebar_com
from routes.auth import is_blacklisted, is_token_expired


def editor_get(sess):
    access_token = sess.get('access_token')
    if not access_token or is_token_expired(access_token):
        sidebar = c.P()
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)
    editor = list_item("Editor", "/editor", "settings"),
    sidebar = sidebar_com()
    tabs = [
        {"name": "Editor", "url": "#"}
    ]


    editor = c.Title("Editor"), c.Div(
        header(sess),
        sidebar,
        c.Div(
            breadcrumb(tabs),
            cls="bg-gray-600 font-inter md:ml-64 p-2",
            id="content",
            style="min-height: 100vh"
        ),
    )
    return editor


