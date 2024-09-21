from apps.cashier.cashier import cashier_get


def cashier_register_routes(app):
    @app.get("/cashier")
    def cashier(sess):
        return cashier_get(sess)

