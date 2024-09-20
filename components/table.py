from fasthtml import common as c


def table_header(headers):
    header_row = c.Tr(
        *[c.Th(header, cls="px-6 py-3 bg-transparent border-none", scope="col") for header in headers]
    )
    return c.Thead(
            header_row,
            cls="text-sm uppercase bg-gray-700 text-gray-400"
        )

def table_row(row_data):
    return [
        c.Td(
            str(item),
            cls="bg-transparent px-6 py-4 text-base",
            scope="row"
        ) for item in row_data
    ]
