from fasthtml.common import A, Button, Div, I, Nav, P, Span


def header(sess):
    access_token = sess.get('access_token')

    user_section = P(cls="hidden")
    if access_token:
        user_section = Div(
            Button(
                Span(sess['username'], cls="hidden sm:block text-white text-lg font-semibold me-4"),
                I(cls="text-2xl rounded-full fas fa-user-alt", style="color: #FFF;"),
                type="button",
                cls="flex text-sm rounded-full focus:ring focus:ring-gray-700 bg-gray-900 border-none hover:bg-gray-800 m-0",
                **{"data-dropdown-toggle": "dropdown-user"}
            ),
            Div(
                Div(
                    Div(
                        Span(f"{sess['first_name']} {sess['last_name']}", cls="text-sm text-white font-semibold mb-1 block"),
                        Span(sess['email'], cls="text-sm font-medium truncate text-gray-300"),
                        cls="px-4 py-3"
                    ),
                ),
                A("Logout", href="/logout", cls="block w-full px-4 py-2 text-sm text-gray-300 hover:bg-red-800 hover:text-white"),
                cls="z-50 hidden my-4 text-base list-none divide-y rounded-lg shadow bg-gray-700 divide-gray-600",
                id="dropdown-user"
            ),
            cls="flex items-center ms-3"
        )

    button = (
        Button(
            Span("Open sidebar", cls="sr-only"),
            I(cls="fa-solid fa-list-ul text-2xl "),
            type="button",
            cls="inline-flex items-center p-2 text-sm md:hidden text-gray-400 bg-gray-900 border-none m-0",
            **{
                "data-drawer-target": "logo-sidebar",
                "data-drawer-toggle": "logo-sidebar",
                "aria-controls": "logo-sidebar"
            }
        )
        if access_token else P()
    )

    return Nav(
        Div(
            Div(
                Div(
                    button,
                    A(
                        I(cls="fa-solid fa-camera mx-2 text-2xl", style="color: #ffffff;"),
                        Span(
                            "Studio Vision",
                            cls=" text-xl font-semibold sm:text-2xl whitespace-nowrap text-white"
                        ),
                        cls="hidden sm:flex ms-2 md:me-24 items-center",
                        href="/"
                    ),
                    cls="flex items-center space-x-4"
                ),
                Div(
                    Div(
                        user_section,
                        cls="flex items-center"
                    ),
                    cls="flex items-center"
                ),
                cls="flex items-center justify-between"
            ),
            cls="px-3 py-3 lg:px-5 lg:pl-3 fixed top-0 z-50 w-full border-b bg-gray-900 border-gray-800"
        )
    )

