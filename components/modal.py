from fasthtml import common as c

from components.button import button


def modal(btn_label,hx_get=None):
    return c.Div(
        c.Div(
            button(
                btn_label,
                hx_get=hx_get,
                hx_target="#modal_content",
                extra={"data-modal-target":"authentication-modal", "data-modal-toggle":"authentication-modal"}
            ),
            cls="my-4",
        ),

        #Modal
        c.Div(
            c.Div(
                c.Div(
                    c.P("Hello"),
                    cls="relative bg-white rounded-lg shadow dark:bg-gray-700",
                    id="modal_content"
                ),
                cls="relative p-4 w-full max-w-md max-h-full"
            ),
            id="authentication-modal", tabindex="-1", **{"aria-hidden":"true"},
            cls="""hidden overflow-y-auto overflow-x-hidden fixed
            top-0 right-0 left-0 z-50 justify-center items-center
            w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"""
        ),
    ),
