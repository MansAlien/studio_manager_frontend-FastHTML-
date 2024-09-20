import os

import requests
from dotenv import load_dotenv
from fasthtml import common as c

from components.table import table_header

load_dotenv()
API_URL = os.getenv('API_URL')

def get_employee_table(sess):
    access_token = sess.get('access_token')

    user_url = f"{API_URL}accounts/user/"
    status_url = f"{API_URL}accounts/logged_in_user/"
    profile_url = f"{API_URL}accounts/user_profile/"
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(user_url, headers=headers)
    profile_response = requests.get(profile_url, headers=headers)
    status_response = requests.get(status_url, headers=headers)
    users_list = []
    online_list = []
    green_icon = c.I(cls="fa-solid fa-circle", style="color: #63E6BE;")
    red_icon = c.I(cls="fa-solid fa-circle", style="color: #f42a2a;")
    if user_response.status_code == 200 and profile_response.status_code == 200:
        user_data = user_response.json()
        profile_data = profile_response.json()
        status_data = status_response.json()
        online_list = [status["user"] for status in status_data if status['is_online'] ]
        for user, profile in zip(user_data, profile_data) :
            id = profile["id"]
            username = user["username"]
            name = f"{user['first_name']} {user['last_name']}".strip()
            age = profile["age"]
            gender = ["Male" if profile["gender"] == "M" else "Femail"]
            salary = profile["salary"]
            job_title = profile["job_title"]
            status = [green_icon if id in online_list else red_icon]
            is_active = [green_icon if user["is_active"] else red_icon]

            user_list = [id, username, name, age, *gender, salary, job_title, *status, *is_active]
            users_list.append(user_list)

    headers = ["ID", "Username", "Name", "Age", "Gender", "Salary", "Job Title", "O/F", "Action"]
    header = table_header(headers)
    rows = [
        c.Tr(
            *[
                c.Td(
                    item,
                    cls="bg-transparent px-6 py-4 text-base",
                    scope="row"
                ) for item in user
            ],
            cls="odd:bg-gray-900 even:bg-gray-800 border-b border-gray-700"
        )for user in users_list
    ]

    return c.Table(
        c.Thead(
            header,
            cls="text-sm uppercase bg-gray-700 text-gray-400"
        ),
        c.Tbody(
            *rows
        ),
        cls="w-full text-sm text-left rtl:text-right text-gray-400"
    )
