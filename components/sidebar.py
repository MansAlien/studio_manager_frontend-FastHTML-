from fasthtml import common as c

def sidebar():
    return c.Aside(
        c.Div(
            cls="h-full px-3 pb-4 overflow-y-auto bg-gray-900 flex flex-col justify-between",
        ),
        id="logo-sidebar",
        cls="""fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full
            border-r-gray-800 md:translate-x-0 bg-gray-900""",
        **{"aria-label": "Sidebar"}
    )

