import os
from typing import Dict, List

from dotenv import load_dotenv
from fasthtml import common as c

from components.table import table_header
from utils.fetch_data import fetch_data

# Constants
load_dotenv()
API_URL = os.getenv('API_URL')
EMPLOYEE_URL = f"{API_URL}accounts/employee-data/"

def get_status_icon(condition: bool):
    """Return a green or red icon based on the condition (e.g., online status)."""
    red_icon = c.I(cls="fa-solid fa-circle", style="color: #f42a2a;")
    green_icon = c.I(cls="fa-solid fa-circle", style="color: #63E6BE;")
    return green_icon if condition else red_icon

def map_gender(gender_code: str) -> str:
    """Map gender codes ('M', 'F') to human-readable strings."""
    return {"M": "Male", "F": "Female"}.get(gender_code, "Unknown")

def build_user_row(employee: Dict, is_superuser_session: bool) -> List:
    """Build a row for the user table with user data, profile data, and online status."""
    is_superuser_user = employee.get("is_superuser")

    # If the session user is not a superuser, we skip superuser rows
    if not is_superuser_session and is_superuser_user:
        return []

    user_id = employee.get("id", "N/A")
    username = employee.get("username", "N/A")
    name = employee.get("name", "N/A")
    age = employee.get("age", "N/A")
    gender = map_gender(employee.get("gender", ""))
    salary = employee.get("salary", "N/A")
    job_title = employee.get("job_title_name", "N/A")
    is_active = get_status_icon(employee.get("is_active", False))
    status = get_status_icon(employee.get("is_online", False))

    return [user_id, username, name, age, gender, salary, job_title, status, is_active]

def get_employee_table(sess: Dict):
    """Build and return the employee table with user data and profile details."""
    access_token = sess.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}

    # Fetch user, profile, and status data
    employee_data = fetch_data(EMPLOYEE_URL, headers)

    if not (employee_data):
        return c.P("Error fetching data. Please try again later.")

    # Check if the current session user is a superuser
    is_superuser_session = sess.get("is_superuser", False)

    # Build table rows, filtering out superusers if the session user is not a superuser
    users_list = [
        build_user_row(employee, is_superuser_session)
        for employee in employee_data
        if build_user_row(employee, is_superuser_session)  # Filter out empty rows
    ]

    # Table headers and rows
    headers = ["ID", "Username", "Name", "Age", "Gender", "Salary", "Job Title", "O/F", "Action"]
    header = table_header(headers)
    rows = [
        c.Tr(
            # ID
            c.Td(
                c.A(
                    user[0] ,  
                    hx_get=f"/settings/employee/detail/{user[0]}",
                    hx_target="#content",
                    hx_swap="innerHTML",
                    cls="font-bold text-gray-200 hover:underline",
                ),
                cls="bg-transparent px-6 py-4 text-base", scope="row"),
            # The rest of the items
            *[c.Td(item, cls="bg-transparent px-6 py-4 text-base", scope="row") for item in user[1:]],
            cls="odd:bg-gray-900 even:bg-gray-800 border-b border-gray-700"
        ) for user in users_list
    ]

    # Return the constructed table
    return c.Table(
        c.Thead(header, cls="text-sm uppercase bg-gray-700 text-gray-400"),
        c.Tbody(*rows),
        cls="w-full text-sm text-left rtl:text-right text-gray-400"
    )
