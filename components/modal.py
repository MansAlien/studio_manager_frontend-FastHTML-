from fasthtml import common as c

from components.button import button

"""
<button type="button" class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="popup-modal">
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                </svg>
                <span class="sr-only">Close modal</span>
            </button>
"""

def modal(btn_label,hx_get=None):
    return c.Div(
        c.Div(
            button(
                btn_label,
                hx_get=hx_get,
                hx_target="#modal_content",
                extra={"data-modal-target":"popup-modal", "data-modal-toggle":"popup-modal"}
            ),
            cls="my-4",
        ),

        #Modal
        c.Div(
            c.Div(
                c.Div(
                    c.Button(
                            c.I(cls="fa-solid fa-x"),
                             **{"data_modal_hide":"popup-modal"},
                        cls="absolute top-3 end-3 border-none"
                    ),
                    c.Div(
                        c.P("Hello"),
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
