from fasthtml.common import Titled, P

def home_get():
    return Titled(
        "FastHTML",
        P("Let's do this!", cls="text-gray-500"),
        P("Hello there!", cls="text-red-600")
    ) 
