from apps.home.home import home_get


def home_register_routes(app):
    @app.get("/")
    def home(sess):
        return home_get(sess)

