from fasthtml.common import Td, Th, Thead, Tr


def table_header(headers):
    header_row = Tr(
        *[Th(header, cls="px-6 py-3 bg-transparent border-none", scope="col") for header in headers]
    )
    return Thead(
            header_row,
            cls="sticky top-0 text-sm uppercase bg-gray-700 text-gray-400"
        )

def table_row(row_data):
    return [
        Td(
            str(item),
            cls="px-6 py-4 text-base",
            scope="row"
        ) for item in row_data
    ]
