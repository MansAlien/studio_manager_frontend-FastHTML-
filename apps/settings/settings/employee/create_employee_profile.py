import os
from typing import Dict

import requests
from dotenv import load_dotenv
from fasthtml import common as c

from apps.auth.auth import is_blacklisted, is_token_expired
from utils.fetch_data import fetch_data

load_dotenv()
API_URL = os.getenv('API_URL')
USER_URL = f"{API_URL}accounts/user/"
JOBTITLE_URL = f"{API_URL}accounts/job_title/"
PROFILE_URL = f"{API_URL}accounts/user_profile/"
CITY_URL = f"{API_URL}accounts/city/"

def get_username_list(users: Dict, key: str):
    """ get the usernames list from the users dict """
    username_list = [user[key] for user in users]
    return username_list

def create_profile_get(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_data = fetch_data(PROFILE_URL, headers)
    jobtitle_data = fetch_data(JOBTITLE_URL, headers)
    city_data = fetch_data(CITY_URL, headers)
    frm = c.Form(
        c.Select(
            c.Option("Select the job title...", selected=True, disabled=True, value=""),
            *[c.Option(job_title["name"]) for job_title in jobtitle_data ],
            name="favorite-cuisine", required=True,
            **{"aria-label":"Select your favorite cuisine..."},
            cls="mb-4 p-2"
        ),
        c.Select(
            c.Option("Select the city...", selected=True, disabled=True, value=""),
            *[c.Option(city["name"]) for city in city_data ],
            name="favorite-cuisine", required=True,
            **{"aria-label":"Select the city..."},
            cls="mb-4 p-2"
        ),
        c.Input(type="date", name="date_of_birth", **{"aria-label":"Date Of Birth"}),
        c.Input(type="date", name="start", **{"aria-label":"Start"}),
        c.Textarea(name="address", placeholder="Write your address",
                   **{"aria-label":"Address"}, cls="p-4 mb-4"),
        c.Input(type="number", name="age", placeholder="Age", **{"aria-label":"Age"}),
        c.Input(type="number", name="salary", placeholder="Salary", **{"aria-label":"Salary"}),
        c.Button('Register', type='submit'),

    )
    return c.Div(
        c.P("Create User Profile", cls="my-2 font-bold text-white"),
        frm,
        c.Div(id='username-error', cls='error-message'),  # This will display the username error
        c.Div(id='result'),
    )

