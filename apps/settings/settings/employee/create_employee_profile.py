import os
from typing import Dict, List

import requests
from dotenv import load_dotenv
from fasthtml import common as c

from components.select_field import select_field
from utils.fetch_data import fetch_data

# Load environment variables
load_dotenv()

# Constants
API_URL = os.getenv('API_URL')
USER_URL = f"{API_URL}accounts/user/"
JOBTITLE_URL = f"{API_URL}accounts/job_title/"
PROFILE_URL = f"{API_URL}accounts/user_profile/"
LAST_PROFILE_URL = f"{API_URL}accounts/user_profile/last_profile/"
CITY_URL = f"{API_URL}accounts/city/"

def get_username_list(users: Dict, key: str) -> List[str]:
    """Get a list of usernames from the user dictionary."""
    return [user.get(key, "") for user in users]

def create_profile_form(jobtitle_data: List[Dict], city_data: List[Dict], genders: List[Dict]):
    """Create a form for user profile creation."""
    return c.Form(
        select_field(jobtitle_data, "job title", "job_title", "Select your job title"),
        select_field(city_data, "city", "city", "Select your city"),
        select_field(genders, "gender", "gender", "Select your gender"),
        c.H2("Birthday: ", cls="mb-1"),
        c.Input(type="date", name="date_of_birth", **{"aria-label": "Date of Birth"}),
        c.H2("Start: ", cls="mb-1"),
        c.Input(type="date", name="start", **{"aria-label": "Start Date"}),
        c.Textarea(
            name="address", placeholder="Write your address",
            **{"aria-label": "Address"}, cls="p-4 mb-4"
        ),
        c.Input(type="number", name="age", placeholder="Age", **{"aria-label": "Age"}),
        c.Input(type="number", name="salary", placeholder="Salary", **{"aria-label": "Salary"}),
        c.Button(
            'Create Profile', type='submit',
            **{"_":"on click add .hidden to #popup-modal then add .hidden to the last <div/> in <body/>"},
        ),
        hx_put="/settings/profile/create", hx_target='#modal_content',
    )

def create_profile_get(access_token: str):
    """Create a modal with a user profile creation form."""
    headers = {'Authorization': f'Bearer {access_token}'}

    # Fetch data for the form
    jobtitle_data = fetch_data(JOBTITLE_URL, headers)
    city_data = fetch_data(CITY_URL, headers)
    genders = [{"id": "M", "name": "Male"}, {"id": "F", "name": "Female"}]

    # Create the form
    form = create_profile_form(jobtitle_data, city_data, genders)

    # Return the page structure
    return c.Div(
        c.P("Create User Profile", cls="my-2 font-bold text-white"),
        form,
        c.Div(id='username-error', cls='error-message'),  # This will display the username error
        c.Div(id='result'),
    )

def create_profile_post(job_title: str, city: str, date_of_birth: str, start: str, address: str, age: str, gender: str, salary: float, access_token: str):
    """Handle form submission and create or update a user profile."""
    
    headers = {'Authorization': f'Bearer {access_token}'}
    
    try:
        # Fetch the last profile data
        last_profile_data = fetch_data(LAST_PROFILE_URL, headers)
    except requests.RequestException as e:
        # Handle fetch failure
        return c.Div(f"Failed to fetch last profile: {str(e)}", id='result', style="color: red;")
    
    # If last profile exists, use its ID, otherwise set ID to None for creation
    profile_id = last_profile_data.get("id") if last_profile_data else None

    # Profile data to send
    data = {
        'id': profile_id,
        'job_title': job_title,
        'city': city,
        'date_of_birth': date_of_birth,
        'start': start,
        'address': address,
        'age': age,
        'gender': gender,
        'user': profile_id,
        'salary': salary,
    }
    
    try:
        # Determine the correct HTTP method based on whether we're updating or creating
        if profile_id:
            # Update existing profile
            response = requests.put(f"{PROFILE_URL}{profile_id}/", json=data, headers=headers)
        else:
            # Create a new profile
            response = requests.post(PROFILE_URL, json=data, headers=headers)
        
        # Handle response based on status code
        if response.status_code in [200, 201]:
            # Success: return the form again or a success message
            return c.Div("Profile saved successfully!", id='result', style="color: green;")
        else:
            # API returned an error, handle and display the message
            error_message = response.json().get('message', "You don't have the privileges.")
            return c.Div(f"Error: {error_message}", id='result', style="color: red;")
    
    except requests.RequestException as e:
        # Handle request failure
        return c.Div(f"Request failed: {str(e)}", id='result', style="color: red;")
