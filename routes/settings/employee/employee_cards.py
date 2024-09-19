import requests
from fasthtml import common as c

from components.cards import status_card


def get_employee_cards(sess):
    access_token = sess.get('access_token')

    #fetch the user_status Data
    user = "http://localhost:8000/api/accounts/user/"
    logged_in = "http://localhost:8000/api/accounts/logged_in_user/"
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(user, headers=headers)
    user_status = requests.get(logged_in, headers=headers)
    online = 0
    active = 0
    offline = 0
    inactive = 0
    if user_response.status_code == 200:
        user_data = user_response.json()
        logged_in_users = user_status.json()
        
        if sess["is_superuser"]:
            active = sum(1 for user in user_data if user['is_active'] )
            inactive = sum(1 for user in user_data if not user['is_active'])
            online = sum(1 for status in logged_in_users if status['is_online'])
            offline = sum(1 for status in logged_in_users if not status['is_online'])
        else:
            active = sum(1 for user in user_data if user['is_active'] and not user['is_superuser'])
            inactive = sum(1 for user in user_data if not user['is_active'] and not user['is_superuser'])
            online = sum(1 for status, user in zip(logged_in_users, user_data) if status['is_online'] and not user["is_superuser"])
            offline = sum(1 for status, user in zip(logged_in_users, user_data) if not status['is_online'] and not user["is_superuser"])

    return c.Div(
        status_card("Online", "online", online),
        status_card("Active", "active", active),
        status_card("Offline", "offline", offline, "red"),
        status_card("Inactive", "inactive", inactive, "red"),
        cls="grid sm:grid-cols-2 md:grid-cols-4 gap-4 mb-4"
    )
