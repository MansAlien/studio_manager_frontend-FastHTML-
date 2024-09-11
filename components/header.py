from fasthtml import common as c

def Header(user):
    """
    Generates a responsive navigation bar. If the user is authenticated, their username and a logout button are displayed.
    
    :param user: Dict containing user information (e.g., is_authenticated, username, first_name, last_name, email).
    :return: A FastHTML component representing the navigation bar.
            <a href="{% url "home" %}" class="flex ms-2 md:me-24 items-center">
          <i class="fa-solid fa-camera mx-2 text-2xl" style="color: #ffffff;"></i>
          <span class="text-xl font-semibold sm:text-2xl whitespace-nowrap text-white">Studio Vision</span>
        </a>

    """
    return c.Nav(
        c.Div(
            c.Div(
                c.Div(
                    c.Div(
                        c.A(
                            c.I(cls="fa-solid fa-camera mx-2 text-2xl", style="color: #ffffff;"),
                            c.Span("Studio Vision", cls="text-xl font-semibold sm:text-2xl whitespace-nowrap text-white"
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
    # Navigation bar structure
    # return Nav(
    #     Div(
    #         Div(
    #             # Sidebar toggle button for mobile
    #             Button(
    #                 Span("Open sidebar", cls="sr-only"),
    #                 I(cls="fa-solid fa-list-ul text-2xl"),
    #                 type="button",
    #                 cls="inline-flex items-center p-2 text-sm rounded-lg md:hidden text-gray-400 hover:bg-gray-700",
    #                 **{"data-drawer-target": "logo-sidebar", "data-drawer-toggle": "logo-sidebar", "aria-controls": "logo-sidebar"}
    #             ),
    #             # Brand logo and name
    #             A(
    #                 I(cls="fa-solid fa-camera mx-2 text-2xl", style="color: #ffffff;"),
    #                 Span("Studio Vision", cls="text-xl font-semibold sm:text-2xl whitespace-nowrap text-white"),
    #                 href="/",  # Change this URL as needed
    #                 cls="flex ms-2 md:me-24 items-center"
    #             ),
    #             cls="flex items-center justify-start rtl:justify-end"
    #         ),
    #         Div(
    #             # User section with username and avatar, conditionally rendered if authenticated
    #             Div(
    #                 Div(
    #                     Div(
    #                         Button(
    #                             Span(user['username'], cls="text-white text-lg font-semibold me-4"),
    #                             I(cls="text-2xl rounded-full fas fa-user-alt", style="color: #FFF;"),
    #                             type="button",
    #                             cls="flex text-sm rounded-full focus:ring focus:ring-gray-700",
    #                             **{"data-dropdown-toggle": "dropdown-user"}
    #                         ),
    #                         # Dropdown menu for user actions (logout)
    #                         Div(
    #                             Div(
    #                                 Span(f"{user['first_name']} {user['last_name']}", cls="text-sm text-white font-semibold mb-1"),
    #                                 Span(user['email'], cls="text-sm font-medium truncate text-gray-300"),
    #                                 cls="px-4 py-3"
    #                             ),
    #                             Form(
    #                                 Button("Logout", type="submit", cls="block w-full px-4 py-2 text-sm text-gray-300 hover:bg-red-800 hover:text-white"),
    #                                 action="/logout", method="post"  # Adjust the logout URL
    #                             ),
    #                             cls="z-50 hidden my-4 text-base list-none divide-y rounded shadow bg-gray-700 divide-gray-600",
    #                             id="dropdown-user"
    #                         ),
    #                         cls="flex items-center ms-3"
    #                     )
    #                 ),
    #                 cls="flex items-center"
    #             ),
    #             cls="flex items-center"
    #         ),
    #         cls="flex items-center justify-between"
    #     ),
    #     cls="fixed top-0 z-50 w-full border-b bg-gray-900 border-gray-800 px-3 py-3 lg:px-5 lg:pl-3"
    # )
    #
    #
