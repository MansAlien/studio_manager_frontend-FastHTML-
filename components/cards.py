from fasthtml.common import A, Div, I, P, Span


def label_card(label, url="#"):
    return Div(
        A(
            label,
            href=url,
            cls="w-full h-full flex justify-center items-center"
        ),
        cls="""flex justify-center items-center bg-gray-800 text-white text-2xl font-bold
                rounded-lg p-4 hover:bg-gray-700 hover:scale-105 hover:shadow-lg hover:rotate-1
                transition duration-300 transform shadow-md hover:text-yellow-300 
                hover:-translate-y-1 hover:text-shadow 
                w-full sm:w-64 md:w-80 lg:w-96
                h-40 sm:h-48 md:h-56 lg:h-64""",
    )

def status_card(label, icon_name, number, color="green"):
    icons = {
        "online": "text-2xl fa-duotone fa-solid fa-signal-bars",
        "active": "text-2xl fa-solid fa-check",
        "offline": "text-2xl fa-duotone fa-solid fa-signal-slash",
        "inactive": "text-2xl fa-solid fa-xmark",
    }
    colors = {
        "green": {
            "text": "text-green-500",
            "border": "border-green-500",
        },
        "red": {
            "text": "text-red-500",
            "border": "border-red-500",
        },
    }

    return Div(
        Span( label, cls=f"{colors[color]['text']} font-bold text-xl "),
        Span(
            P(number, cls="text-xl"),
            I(cls=icons[icon_name]),
            cls="flex justify-between items-center text-white  pt-4 px-2"
        ),
        cls=f"h-28 rounded bg-gray-800 border-l-4 {colors[color]['border']} p-4"
    )
