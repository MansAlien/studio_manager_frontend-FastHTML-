from fasthtml.common import Button, Div, I, P

from components.button import button


def modal(btn_label,hx_get=None):
    return Div(
        Div(
            button(
                btn_label,
                hx_get=hx_get,
                hx_target="#modal_content",
                extra={"data-modal-target":"popup-modal", "data-modal-toggle":"popup-modal"}
            ),
            cls="my-4",
        ),

        #Modal
        Div(
            Div(
                Div(
                    Button(
                            I(cls="fa-solid fa-x"),
                             **{"data_modal_hide":"popup-modal"},
                        cls="absolute top-3 end-3 border-none"
                    ),
                    Div(
                        P("Hello"),
                        id="modal_content",
                        cls="p-5 pt-6"
                    ),

                    cls="relative bg-white rounded-lg shadow dark:bg-gray-700",
                ),
                cls="relative p-4 w-full max-w-md max-h-full"
            ),
            id="popup-modal", tabindex="-1",
            cls="""hidden overflow-y-auto overflow-x-hidden fixed
            top-0 right-0 left-0 z-50 justify-center items-center
            w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"""
        ),
    ),
