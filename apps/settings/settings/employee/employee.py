from fasthtml import common as c

from apps.auth.auth import is_blacklisted, is_token_expired
from components.breadcrumb import breadcrumb
from components.modal import modal


def build_cards_section():
    """Build the cards section that auto-updates every 5 seconds."""
    return c.Div(
        cls="row row-cols-1 row-cols-sm-2 row-cols-md-4 g-3",
        id="cards",
        hx_get="/settings/employee/cards",
        hx_swap="innerHTML",
        hx_trigger="load, every 5s",
        hx_target="this"
    )


def build_table_section():
    """Build the table section to display employee data."""
    return c.Div(
        cls="relative overflow-x-auto shadow-md sm:rounded-lg my-4 h-[55%]",
        hx_get="/settings/employee/table",
        hx_swap="innerHTML",
        hx_trigger="load, htmx:afterRequest from:#modal_content",
        hx_target="this",
        id="employee_table",
    )


def employee_get(access_token):
    """Build and return the employee page with status cards, profile details, and a table."""

    # Handle missing or invalid tokens
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)

    # Define breadcrumb tabs
    tabs = [
        {"name": "Settings", "url": "/settings"},
        {"name": "Employee", "url": "#"}
    ]

    # Build the employee page structure
    employee_page = c.Div(
        breadcrumb(tabs),

        # Status cards section
        build_cards_section(),

        modal("Create Employee", hx_get="/settings/employee/create"),

        # Employee table section
        build_table_section(),

        cls="bg-gray-600 font-inter p-2 h-screen",
        id="content",
        style="min-height: 100vh"
    )
    
    return employee_page

