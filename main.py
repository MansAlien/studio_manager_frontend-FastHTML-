# fasthtml_main.py in FastHTML
from fasthtml.common import (
    Link,
    fast_app,
    serve,
    H3,
    Div,
    Button,
    P,
    Titled,
)
import requests

app, rt = fast_app(hdrs=(Link(rel="stylesheet", href="/static/src/output.css"),))

@rt("/")
def index():
    return Titled("Governorates List",
        Div(id="governorates-container", cls="mt-8"),
        Button("Load Governorates", cls="bg-blue-500 text-white py-2 px-4 rounded", hx_get="/api/governorates/", hx_target="#governorates-container", hx_swap="innerHTML"),
    )

@rt("/api/governorates/")
def fetch_governorates():
    # Fetch governorates data from Django API
    response = requests.get("http://localhost:8000/api/accounts/governorate/")
    governorates = response.json()

    # Build the HTML for each governorate as a card using Tailwind CSS
    cards = [
        Div(
            H3(governorate['name'], cls="text-lg font-bold mb-2"),
            P(f"Population: {governorate['id']}", cls="text-sm text-gray-600"),
            cls="bg-white shadow-md rounded-lg p-4 mb-4"
        ) for governorate in governorates
    ]
    
    # Wrap the cards in a container div
    return Div(*cards, cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6")

serve()

