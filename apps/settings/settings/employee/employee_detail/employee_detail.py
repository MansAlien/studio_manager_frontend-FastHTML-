from fasthtml import common as c

from apps.auth.auth import is_blacklisted, is_token_expired
from components.breadcrumb import breadcrumb
from components.modal import modal


def employee_detail_get(id, access_token):
    """Build and return the employee page with status cards, profile details, and a table."""

    # Handle missing or invalid tokens
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)

    tabs = [
        {"name": "Settings", "url": "/settings"},
        {"name": "Employee", "url": "/settings"},
        {"name": "Details", "url": "#"}
    ]

    employee_detail = c.Div(
        breadcrumb(tabs),
        c.H1(id),
        cls="bg-gray-600 font-inter p-2 h-screen",
        id="content",
        style="min-height: 100vh"
    )
    return employee_detail
