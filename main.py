from fasthtml.common import fast_app, serve, Link
from routes.home import home_get

app, rt = fast_app(hdrs=(Link(rel="stylesheet", href="/static/css/output.css"),))

@rt("/")
def home():
    return home_get()

serve()
