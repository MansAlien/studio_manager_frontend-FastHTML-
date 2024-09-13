from fasthtml import common as c 
"""
    <nav class="flex my-2 mt-12 p-4" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse">
        <li class="inline-flex items-center space-x-1 text-gray-400 ">
          <i class=" fas fa-home"></i>
          <span class="ms-1 text-sm font-medium md:ms-2 text-gray-400">
            Home
          </span>
        </li>
      </ol>
    </nav>
"""

def breadcrumb(tabs: list = None):
    tabs = tabs or []
    # Generate the breadcrumb items
    items = [
        c.Li(
            c.Span(">"),
            c.A(
                tab["name"],
                href=tab.get("url", "#"),  # Fallback to '#' if no URL is provided
                cls="text-sm font-medium text-gray-400 hover:text-white"
            ),
            cls="inline-flex items-center space-x-1 text-gray-400 p-0"
        ) for tab in tabs
    ]

    # Insert home icon as the first item
    items.insert(0, 
         c.Li(
             c.A(c.Span(cls="fas fa-home hover:text-white"), href="/", cls="inline-flex items-center"),
             cls="inline-flex items-center space-x-1 text-gray-400 ms-1"
         )
    )

    # Return the complete breadcrumb navigation
    return c.Nav(
        c.Ol(*items, cls="inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse"),
        cls="flex my-2 mt-12 py-5",
        **{"aria-label": "Breadcrumb"}
    )
