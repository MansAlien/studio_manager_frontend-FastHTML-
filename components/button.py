from fasthtml import common as c


def button(label, color="default"):
    styles = {
        "default": "text-white bg-blue-600 hover:bg-blue-700 focus:ring-blue-800",
        "alternative": "text-gray-400 bg-gray-800 border border-gray-600 hover:text-white hover:bg-gray-700",
        "dark": "text-white bg-gray-800 hover:bg-gray-700 focus:ring-gray-700 border-gray-700",
        "light": "text-white bg-gray-800 border border-gray-600 hover:bg-gray-700 hover:border-gray-600 focus:ring-gray-700",
        "green": "text-white bg-green-600 hover:bg-green-700 focus:ring-green-800",
        "red": "text-white bg-red-600 hover:bg-red-700 focus:ring-red-900",
        "yellow": "text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-yellow-900",
        "purple": "text-white bg-purple-600 hover:bg-purple-700 focus:ring-purple-900",
    }
    return  c.Button(
        label,
        type="button",
        cls=f"{styles[color]} focus:outline-none font-medium rounded-lg text-base px-5 py-2.5 me-2 mb-2 border-transparent",
    )
