import os
import requests

from typing import Dict

from dotenv import load_dotenv
from fasthtml import common as c

from apps.auth.auth import is_blacklisted, is_token_expired
from utils.fetch_data import fetch_data

load_dotenv()
API_URL = os.getenv('API_URL')
USER_URL = f"{API_URL}accounts/user/"

def get_username_list(users: Dict, key: str):
    """ get the usernames list from the users dict """
    username_list = [user[key] for user in users]
    return username_list

def create_employee_get(access_token: str):
    """Build and return the create employee form and checking the validation of (username, email, password)."""
    headers = {'Authorization': f'Bearer {access_token}'}
    if not access_token or is_token_expired(access_token):
        return c.RedirectResponse('/logout', status_code=303)
    elif is_blacklisted(access_token):
        return c.RedirectResponse('/logout/blacklist', status_code=303)

    # Fetch the user data and get the username list
    user_data = fetch_data(USER_URL, headers)
    username_list = get_username_list(user_data, "username")
    email_list = get_username_list(user_data, "email")

    frm = c.Form(
        c.Input(type="text", name="username",
                placeholder="Username", autocomplete="email",
                **{
                "aria-label": "username",
                "aria-invalid": "",
                "aria-describedby":"invalid-helper",
                "_": f"""
                            on keyup 
                            for x in {username_list}
                                if my.value == x
                                    set my @aria-invalid to 'true'
                                    put 'Username is already taken' into #invalid-username
                                    break
                                else
                                    set my @aria-invalid to 'false'
                            end
                        """
                }),
        c.Small(id="invalid-username"),
        c.Input(type="text", name="first_name", placeholder="First Name", autocomplete="email", **{"aria-label":"first_name"}),
        c.Input(type="text", name="last_name", placeholder="Last Name", autocomplete="email", **{"aria-label":"last_name"}),
        c.Input(type="email", name="email",
                placeholder="Email", autocomplete="email",
                **{
                "aria-label":"email",
                "aria-invalid": "",
                "aria-describedby":"invalid-helper",
                "_": f"""
                            on keyup 
                            for x in {email_list}
                                if my.value == x
                                    set my @aria-invalid to 'true'
                                    put 'Email is already taken' into #invalid-email
                                    break
                                else
                                    set my @aria-invalid to 'false'
                            end
                        """
                }),
        c.Small(id="invalid-email"),
        c.Input(type="password", name="password",
                placeholder="Password", id="password",
                **{"aria-label":"password", "aria-invalid":"",}),
        c.Input(type="password", name="confirm",
                placeholder="Password Confirm",
                id="confirm",
                **{
                "aria-label":"confirm",
                "aria-invalid":"",
                "_":"""
                        on keyup 
                        if #password.value != my.value
                        set my @aria-invalid to 'true' 
                        set #password's @aria-invalid to ''
                        else set my @aria-invalid to 'false'
                        set #password's @aria-invalid to 'false'
                        """,
                },),
        c.Button('Register', type='submit'),
        action='/settings/employee/create', method='post', hx_post="/settings/employee/create", hx_target='#result',
    )

    return c.Div(
        c.P("Create User Account", cls="my-2 font-bold text-white"),
        frm,
        c.Div(id='username-error', cls='error-message'),  # This will display the username error
        c.Div(id='result'),
    )

def create_employee_post(username: str, first_name: str, last_name: str, email: str, password: str, confirm: str, access_token: str):
    """Handle form submission and create a new employee."""
    
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # Fetch existing users to double-check username and email availability
    user_data = fetch_data(USER_URL, headers)
    if user_data:
        username_list = [user['username'] for user in user_data]
        email_list = [user['email'] for user in user_data]
    else:
        return

    # Check if username or email already exists (server-side validation)
    if username in username_list:
        return c.Div("Username is already taken", id='result', style="color: red;")
    if email in email_list:
        return c.Div("Email is already taken", id='result', style="color: red;")

    # Check if passwords match
    if password != confirm:
        return c.Div("Passwords do not match", id='result', style="color: red;")
    
    # Send the data to the API to create the user
    data = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
    }
    
    try:
        # Make the API call to register the user
        response = requests.post(USER_URL, json=data, headers=headers)
        
        if response.status_code == 201:
            # Success: return a success message
            return c.Div("Employee created successfully!", id='result', style="color: green;")
        else:
            # Handle errors returned by the API
            return c.Div(f"Error: {response.json().get('message', "You don't have the privileges")}", id='result', style="color: red;")
    
    except requests.RequestException as e:
        # Handle request failure
        return c.Div(f"Request failed: {str(e)}", id='result', style="color: red;")
