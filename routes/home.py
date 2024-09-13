from fasthtml import common as c
from components.header import Header
from components.sidebar import sidebar

def home_get(sess):
    access_token = sess.get('access_token')
    if not access_token:
        Sidebar = c.P()
        return c.RedirectResponse('/login', status_code=303)
    else:
        Sidebar = sidebar()

    return c.Title("Studio Vision"), c.Div(
        Header(sess),
        Sidebar,
        c.Div(
        ),
        c.Div(
            # Add a logout button
            c.A("Logout",
                href="/logout",
                cls="bg-red-500 text-white py-2 px-4 rounded mt-4",
                ),
            cls="flex justify-end"
        ),
        cls="bg-gray-600 h-screen font-inter"
    ) 
