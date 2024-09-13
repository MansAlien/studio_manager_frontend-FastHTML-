from fasthtml import common as c
"""
    <ul class="space-y-2 font-medium">
      <li>
        <form action="{% url 'logout' %}" method="post" >
          {% csrf_token %}
          <button type="submit" class="flex w-full items-top p-2 rounded-lg 
            text-white hover:bg-red-800 group">
              <span class="inline-block w-5 h-5 transition duration-75 
                text-gray-200 group-hover:text-white">
                  <i class="text-xl fa-solid fa-right-from-bracket"></i>
              </span>
            <span class="ms-5 text-gray-300 text-lg">Logout</span>
          </button>
        </form>
      </li>
    </ul>
"""

def list_item(label, url, icon_name, hover_color="gray"):
    icons = {
        "settings": "text-xl fa-solid fa-gear",
        "logout": "text-xl fa-solid fa-right-from-bracket",
    }
    hover_colors = {
        "gray": "hover:bg-gray-700",
        "red": "hover:bg-red-800",
    }
    return c.Li(
        c.A(
            c.Span(
                c.I(cls=icons[icon_name]),
                cls="inline-block w-5 h-5 transition duration-75 text-gray-200 group-hover:text-white"
            ),
            c.Span(label, cls="ms-5 text-gray-300 text-lg "),
            href=url,
            cls=f"flex items-top p-2 rounded-lg text-white {hover_colors[hover_color]} group"
        ),
        cls="w-full px-1 py-0"
    )


def sidebar():
    return c.Aside(
        c.Div(
            c.Ul(
                c.Li("hello"),
                c.Li("hello"),
                cls="space-y-2 font-medium"
            ),
            c.Ul(
                c.Li("hello"),
                c.Li("hello"),
                cls="space-y-2 font-medium"
            ),
            c.Ul(
                list_item("settings", "#", "settings"),
                list_item("logout", "/logout", "logout", "red"),
                cls="space-y-2 font-medium"
            ),
            cls="h-full px-0 pb-4 overflow-y-auto bg-gray-900 flex flex-col justify-between",
        ),
        id="logo-sidebar",
        cls="""fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full
            border-r-gray-800 md:translate-x-0 bg-gray-900""",
        **{"aria-label": "Sidebar"}
    )

