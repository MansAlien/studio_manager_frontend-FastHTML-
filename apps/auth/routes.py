from apps.auth.auth import (
    LoginForm,
    login_get_route,
    login_post_route,
    logout_blacklist,
    logout_route,
)


def auth_register_routes(app):
    @app.get("/login")
    def login_get(sess):
        return login_get_route(sess)

    @app.post("/login")
    def login_post(login: LoginForm, sess):
        return login_post_route(login, sess)

    @app.get("/logout")
    def logout_rout(sess):
        return logout_route(sess)

    @app.get("/logout/blacklist")
    def logout_blacklist_route(sess):
        return logout_blacklist(sess)
