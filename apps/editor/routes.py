from apps.editor.editor import editor_get


def editor_register_routes(app):
    @app.get("/editor")
    def editor(sess):
        return editor_get(sess)

