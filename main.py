import uvicorn
from fasthtml.common import Link, Script, fast_app, serve

from routes.auth import LoginForm, login_get_route, login_post_route, logout_route
from routes.cashier import cashier_get
from routes.editor import editor_get
from routes.home import home_get
from routes.settings import settings_get

# links
favicon = Link(rel="icon", href="/static/img/favicon.ico", type="image/x-icon")
style = Link(rel="stylesheet", href="/static/css/output.css")
font_awesome = Link(rel="stylesheet", href="/static/css/all.min.css")
flowbite = Script(src="/static/js/flowbite.min.js")

app, rt = fast_app(hdrs=( favicon, style, font_awesome, flowbite ))

@rt("/login", methods=["GET"])
def login_get():
    return login_get_route()

@rt("/login", methods=["POST"])
def login_post(login: LoginForm, sess):
    return login_post_route(login, sess)

@rt("/logout")
def logout_rout(sess):
    return logout_route(sess)

@rt("/")
def home(sess):
    return home_get(sess)

@rt("/settings")
def settings(sess):
    return settings_get(sess)

@rt("/editor")
def editor(sess):
    return editor_get(sess)

@rt("/cashier")
def cashier(sess):
    return cashier_get(sess)

serve()
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5001)

