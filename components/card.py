from fasthtml.common import (
    Div,
    H2,
    P,
)

def create_card(id, text, color):
    card = Div(
        H2(f"Card {id}", style="color: black;"),
        P(f"This is card number {text}", style="color: black;"),
        cls="card",
        style=f"background-color: {color}; margin: 10px; padding: 20px; border-radius: 8px;"
    )
    return card
