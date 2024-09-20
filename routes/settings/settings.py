from typing import Dict, List

from fasthtml import common as c

from components.header import header
from components.sidebar import list_item, sidebar_com
from routes.auth import is_blacklisted, is_token_expired


def build_sidebar_items() -> List:
    """Build and return a list of sidebar items for settings."""
    employee = list_item(
        "Employee", "#", "dynamic", hx_get="/settings/employee", hx_target="#content", hx_swap="innerHTML"
    )
    inventory = list_item(
        "Inventory", "#", "dynamic", hx_get="/settings/inventory", hx_target="#content", hx_swap="innerHTML"
    )
    orders = list_item(
        "Orders", "#", "dynamic", hx_get="/settings/orders", hx_target="#content", hx_swap="innerHTML"
    )
    return [employee, inventory, orders]


def settings_get(sess: Dict):
    """Build and return the settings page with a header, sidebar, and content."""
    access_token = sess.get('access_token')

    # Handle expired or blacklisted tokens
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)

    # Sidebar items
    items = build_sidebar_items()
    sidebar = sidebar_com(items)

    # Page layout with header, sidebar, and content
    settings_page = c.Div(
        c.Title("Settings"),  # Page title
        header(sess),  # Header component
        sidebar,  # Sidebar with menu items
        c.Div(  # Main content section
            cls="bg-gray-600 font-inter md:ml-64",
            id="content",
            style="min-height: 94vh",
            hx_get="/settings/employee",
            hx_swap="innerHTML",
            hx_trigger="load",
            hx_target="this"
        ),
    )
    
    return settings_page

