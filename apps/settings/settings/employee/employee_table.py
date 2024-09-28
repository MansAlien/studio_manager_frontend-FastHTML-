import os
from typing import Dict, List

from dotenv import load_dotenv
from fasthtml import common as c

from components.table import table_header
from utils.fetch_data import fetch_data

# Constants
load_dotenv()
API_URL = os.getenv('API_URL')
USER_URL = f"{API_URL}accounts/user/"
STATUS_URL = f"{API_URL}accounts/logged_in_user/"
PROFILE_URL = f"{API_URL}accounts/user_profile/"

def get_status_icon(condition: bool):
    """Return a green or red icon based on the condition (e.g., online status)."""
    red_icon = c.I(cls="fa-solid fa-circle", style="color: #f42a2a;")
    green_icon = c.I(cls="fa-solid fa-circle", style="color: #63E6BE;")
    return green_icon if condition else red_icon

def map_gender(gender_code: str) -> str:
    """Map gender codes ('M', 'F') to human-readable strings."""
    return {"M": "Male", "F": "Female"}.get(gender_code, "Unknown")

def build_user_row(user: Dict, profile: Dict, online_list: List[int], is_superuser_session: bool):
    """Build a row for the user table with user data, profile data, and online status."""
    is_superuser_user = user.get("is_superuser")

    # If the session user is not a superuser, we skip superuser rows
    if not is_superuser_session and is_superuser_user:
        return []

    user_id = profile.get("id", "N/A")
    username = user.get("username", "N/A")
    name = f"{user.get('first_name', '')} {user.get('last_name', '')}".strip()
    age = profile.get("age", "N/A")
    gender = map_gender(profile.get("gender", ""))
    salary = profile.get("salary", "N/A")
    job_title = profile.get("job_title_name", "N/A")
    status = get_status_icon(user_id in online_list)
    is_active = get_status_icon(user.get("is_active", False))

    return [user_id, username, name, age, gender, salary, job_title, status, is_active]

def get_employee_table(sess: Dict):
    """Build and return the employee table with user data and profile details."""
    access_token = sess.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}

    # Fetch user, profile, and status data
    user_data = fetch_data(USER_URL, headers)
    profile_data = fetch_data(PROFILE_URL, headers)
    status_data = fetch_data(STATUS_URL, headers)

    if not (user_data and profile_data and status_data):
        return c.P("Error fetching data. Please try again later.")

    # Extract online user IDs from status data
    online_list = [status.get("user") for status in status_data if status.get('is_online')]

    # Check if the current session user is a superuser
    is_superuser_session = sess.get("is_superuser", False)

    # Build table rows, filtering out superusers if the session user is not a superuser
    users_list = [
        build_user_row(user, profile, online_list, is_superuser_session)
        for user, profile in zip(user_data, profile_data)
        if build_user_row(user, profile, online_list, is_superuser_session)  # Filter out empty rows
    ]

    # Table headers and rows
    headers = ["ID", "Username", "Name", "Age", "Gender", "Salary", "Job Title", "O/F", "Action"]
    header = table_header(headers)
    rows = [
        c.Tr(
            *[c.Td(item, cls="bg-transparent px-6 py-4 text-base", scope="row") for item in user],
            cls="odd:bg-gray-900 even:bg-gray-800 border-b border-gray-700"
        ) for user in users_list
    ]

    # Return the constructed table
    return c.Table(
        c.Thead(header, cls="text-sm uppercase bg-gray-700 text-gray-400"),
        c.Tbody(*rows),
        cls="w-full text-sm text-left rtl:text-right text-gray-400"
    )
