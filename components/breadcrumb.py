from fasthtml.common import A, Li, Nav, Ol, Span


def breadcrumb(tabs: list = None):
    tabs = tabs or []
    items = [
        Li(
            Span(">", style="cursor: default"),
            A(
                tab["name"],
                href=tab.get("url", "#"),
                cls="text-sm font-medium text-gray-400 hover:text-white"
            ),
            cls="inline-flex items-center space-x-1 text-gray-400 p-0"
        ) for tab in tabs
    ]

    items.insert(0, 
         Li(
             A(Span(cls="fas fa-home hover:text-white"), href="/", cls="inline-flex items-center"),
             cls="inline-flex items-center space-x-1 text-gray-400 ms-1"
         )
    )

    return Nav(
        Ol(*items, cls="inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse"),
        cls="flex my-2 mt-12 py-5",
        **{"aria-label": "Breadcrumb"}
    )
