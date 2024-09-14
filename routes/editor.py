from fasthtml import common as c
from components.breadcrumb import breadcrumb

def editor_get(sess):
    access_token = sess.get('access_token')
    if not access_token:
        return c.RedirectResponse('/login', status_code=303)
    else:
        tabs = [
            {"name": "Editor", "url": "#"}
        ]

    settings =  c.Div(
        c.Div(
            breadcrumb(tabs),
        ),
    ) 
    return settings

