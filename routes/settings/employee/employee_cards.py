import os
from typing import Dict

from dotenv import load_dotenv
from fasthtml import common as c

from components.cards import status_card
from utils.fetch_data import fetch_data

# Constants
load_dotenv()
API_URL = os.getenv('API_URL')
USER_URL = f"{API_URL}accounts/user/"
LOGGEDIN_USER_URL = f"{API_URL}accounts/logged_in_user/"

def get_employee_cards(sess: Dict):
    """Build and return employee status cards (Online, Active, Offline, Inactive)."""
    access_token = sess.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}

    # Fetch the user and logged-in status data
    user_data = fetch_data(USER_URL, headers)
    logged_in_users_data = fetch_data(LOGGEDIN_USER_URL, headers)
    if not (user_data and logged_in_users_data):
        return c.P("Error fetching data. Please try again later.")

    # Count status based on the user role
    if sess["is_superuser"]:
        active = sum(1 for user in user_data if user['is_active'] )
        inactive = sum(1 for user in user_data if not user['is_active'])
        online = sum(1 for status in logged_in_users_data if status['is_online'])
        offline = sum(1 for status in logged_in_users_data if not status['is_online'])
    else:
        active = sum(1 for user in user_data if user['is_active'] and not user['is_superuser'])
        inactive = sum(1 for user in user_data if not user['is_active'] and not user['is_superuser'])
        online = sum(1 for status, user in zip(logged_in_users_data, user_data) if status['is_online'] and not user["is_superuser"])
        offline = sum(1 for status, user in zip(logged_in_users_data, user_data) if not status['is_online'] and not user["is_superuser"])

    # Return status cards grid
    return c.Div(
        status_card("Online", "online", online),
        status_card("Active", "active", active),
        status_card("Offline", "offline", offline, "red"),
        status_card("Inactive", "inactive", inactive, "red"),
        cls="grid sm:grid-cols-2 md:grid-cols-4 gap-4 mb-4"
    )
