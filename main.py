from fasthtml.common import fast_app, serve, Link, P
from routes.home import home_get
import uvicorn

app, rt = fast_app(hdrs=(Link(rel="stylesheet", href="/static/css/output.css"),))

@rt("/")
def home():
    return home_get()
    # return P("Hello", cls="text-red-500")

serve()
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)
