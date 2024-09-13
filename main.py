from fasthtml.common import fast_app, serve, Link, Script
from routes.home import home_get
from routes.settings import settings_get
from routes.auth import LoginForm, login_get_route, login_post_route, logout_route
import uvicorn

# Create the FastHTML app
app, rt = fast_app(hdrs=(
    Link(rel="stylesheet", href="/static/css/output.css"),
    Link(rel="stylesheet", href="/static/css/all.min.css"),
    Script(src="/static/js/flowbite.min.js"),
))

# Login route for GET request (renders the login form)
@rt("/login", methods=["GET"])  # Specify GET method
def login_get(sess):
    return login_get_route(sess)

# Login route for POST request (handles form submission)
@rt("/login", methods=["POST"])  # Specify POST method
def login_post(login: LoginForm, sess):
    return login_post_route(login, sess)

# Logout route
@rt("/logout")
def logout_rout(sess):
    return logout_route(sess)

# Home route (protected)
@rt("/")
def home(sess):
    return home_get(sess)

@rt("/settings")
def settings(sess):
    return settings_get(sess)
# Serve the app
serve()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)

