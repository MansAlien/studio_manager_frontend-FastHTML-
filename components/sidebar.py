from fasthtml.common import A, Aside, Div, I, Li, P, Span, Ul


def list_item(label, url=None, icon_name=None, hover_color="gray", hx_get=None, hx_swap=None, hx_target=None):
    icons = {
        "settings": "text-xl fa-solid fa-gear",
        "home": "text-xl fas fa-home",
        "upload": "text-xl fa-solid fa-upload",
        "logout": "text-xl fa-solid fa-right-from-bracket",
        "dynamic": "text-xl fa-solid fa-circle-plus",
    }
    hover_colors = {
        "gray": "hover:bg-gray-700",
        "red": "hover:bg-red-800",
    }

    attrs = { "cls": f"flex items-top p-2 rounded-lg text-white {hover_colors[hover_color]} group",
        "href": url,  # Traditional link
    }
    
    if hx_get:
        attrs["hx-get"] = hx_get
    if hx_swap:
        attrs["hx-swap"] = hx_swap
    if hx_target:
        attrs["hx-target"] = hx_target
    
    if hx_get:
        attrs.pop("href", None)

    item = Li(
        A(
            Span(
                I(cls=icons.get(icon_name, "text-xl fa-solid fa-link")),
                cls="inline-block w-5 h-5 transition duration-75 text-gray-200 group-hover:text-white"
            ),
            Span(label, cls="ms-5 text-gray-300 text-lg"),
            **attrs),
        cls="w-full px-1 py-0"
    )
    
    return item

def sidebar_com(items: list = None):
    if not items:
        items = [P(cls="hidden")]
    return Aside(
        Div(
            Ul(
                list_item("Home", "/", "home"),
                list_item("Upload", "#", "upload"),
                cls="space-y-2 font-medium"
            ),
            # Dynamic content
            Ul(
                *items,
                cls="space-y-2 font-medium"
            ),
            Ul(
                list_item("Settings", "/settings", "settings"),
                list_item("Logout", "/logout", "logout", "red"),
                cls="space-y-2 font-medium"),
            cls="h-full px-0 pb-4 overflow-y-auto bg-gray-900 flex flex-col justify-between",
        ),
        id="logo-sidebar",
        cls="""fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full
            border-r-gray-800 md:translate-x-0 bg-gray-900""",
        **{"aria-label": "Sidebar"}
    )

