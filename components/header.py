from fasthtml import common as c

def Header():
    """
        <button data-drawer-target="logo-sidebar" data-drawer-toggle="logo-sidebar" aria-controls="logo-sidebar"
          type="button" class="inline-flex items-center p-2 text-sm rounded-lg md:hidden 
          focus:outline-none focus:ring-2 text-gray-400 hover:bg-gray-700 focus:ring-gray-600">
          <span class="sr-only">Open sidebar</span>
          <i class="fa-solid fa-list-ul text-2xl"></i>
        </button>
    """
    return c.Nav(
        c.Div(
            c.Div(
                c.Div(
                    c.Div(
                        c.Button(
                            c.Span("Open sidebar", cls="sr-only"),
                            c.I(cls="fa-solid fa-list-ul text-2xl"),
                            type="button",
                            cls="inline-flex items-center p-2 text-sm rounded-lg md:hidden text-gray-400 hover:bg-gray-700",
                            **{
                                "data-drawer-target": "logo-sidebar",
                                "data-drawer-toggle": "logo-sidebar",
                                "aria-controls": "logo-sidebar"
                            }
                        ),
                        c.A(
                            c.I(cls="fa-solid fa-camera mx-2 text-2xl", style="color: #ffffff;"),
                            c.Span(
                                "Studio Vision",
                                cls="text-xl font-semibold sm:text-2xl whitespace-nowrap text-white"
                                   ),
                            cls="flex ms-2 md:me-24 items-center",
                            href="/"
                        )
                    ),
                    cls="flex items-center justify-start rtl:justify-end"
                ),
                cls="flex items-center justify-between"
            ),
            cls="px-3 py-3 lg:px-5 lg:pl-3"
        ),
        cls="fixed top-0 z-50 w-full border-b bg-gray-900 border-gray-800"
    )
