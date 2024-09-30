from fasthtml.common import Option, Select


def select_field(data, placeholder, name, aria_label, cls="mb-4 p-2"):
    """Generate a select field with options."""
    return Select(
        Option(f"Select the {placeholder}...", selected=True, disabled=True, value=""),
        *[Option(item["name"], value=item["id"]) for item in data],
        name=name, required=True,
        **{"aria-label": aria_label},
        cls=cls
    )
