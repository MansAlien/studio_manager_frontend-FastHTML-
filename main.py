import uvicorn
from fasthtml.common import Link, Script, fast_app, serve

from apps.auth.routes import auth_register_routes
from apps.cashier.routes import cashier_register_routes
from apps.editor.routes import editor_register_routes
from apps.home.routes import home_register_routes
from apps.settings.routes import settings_register_routes

# links
favicon = Link(rel="icon", href="/static/img/favicon.ico", type="image/x-icon")
font_awesome_css = Link(rel="stylesheet", href="/static/css/all.min.css")
font_awesome_js = Script(src="/static/js/all.min.js")
flowbite = Script(src="/static/js/flowbite.min.js")
hyper = Script(src="/static/js/_hyperscript.min.js")
tailwind_cdn = Script(src="/static/js/tailwind_cdn.js")

app, rt = fast_app(hdrs=(favicon, tailwind_cdn, font_awesome_css, font_awesome_js, flowbite, hyper ))

auth_register_routes(app)
home_register_routes(app)
cashier_register_routes(app)
editor_register_routes(app)
settings_register_routes(app)


serve()
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5001)

