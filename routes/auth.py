from fasthtml.common import dataclass
from fasthtml import common as c
import requests
import os
from dotenv import load_dotenv
import jwt

from components.header import Header

def login_get_route(sess):
    frm = c.Form(
        c.P("Username", cls="my-1 font-bold text-white text-sm"),
        c.Input(
            id='username',
            placeholder='Username',
            cls="""border text-sm rounded-lg block w-full
            p-2.5 bg-gray-800 border-gray-600 placeholder-gray-400
            text-white focus:ring-blue-500 focus:border-blue-500"""
        ),
        c.P("Password", cls="my-1 font-bold text-white text-sm"),
        c.Input(
            id='password',
            type='password',
            placeholder='Password',
            cls="""border text-sm rounded-lg block w-full
            p-2.5 bg-gray-800 border-gray-600 placeholder-gray-400
            text-white focus:ring-blue-500 focus:border-blue-500"""
        ),
        c.Button('Login', type="submit", cls="w-full bg-blue-500 text-white p-2 rounded"),
        action='/login', method='post'
    )

    return c.Div(
        c.Div(
            c.Div(
                frm,
                cls="sm:bg-gray-700 p-6 rounded-lg w-full max-w-sm"  # Set a max-width and full width on small screens
            ),
            cls="flex h-full w-full justify-center items-center"
        ),
        cls="bg-gray-600 font-inter h-screen w-screen"  # Add padding to the sides for small screens
    )

@dataclass
class LoginForm:
    username: str
    password: str

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def login_post_route(login: LoginForm, sess):
    jwt_url = "http://localhost:8000/api/token/"
    payload = {'username': login.username, 'password': login.password}

    response = requests.post(jwt_url, json=payload)

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get("access")
        refresh_token = tokens.get("refresh")

        try:
            decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token.get('user_id')  # Extract user ID from the decoded token
        except jwt.InvalidTokenError:
            return c.RedirectResponse('/login', status_code=303)

        #fetch user_data
        user_details_url = f"http://localhost:8000/api/accounts/user/{user_id}/"
        headers = {'Authorization': f'Bearer {access_token}'}
        user_response = requests.get(user_details_url, headers=headers)

        if user_response.status_code == 200:
            user_data = user_response.json()
            # Extract and save user information in the session
            sess['access_token'] = access_token
            sess['refresh_token'] = refresh_token
            sess['username'] = user_data.get('username')
            sess['first_name'] = user_data.get('first_name')
            sess['last_name'] = user_data.get('last_name')
            sess['email'] = user_data.get('email')

        return c.RedirectResponse('/', status_code=303)
    else:
        return c.RedirectResponse('/login', status_code=303)

def logout_route(sess):
    sess.pop('access_token', None)
    sess.pop('refresh_token', None)
    sess.pop('first_name', None)
    sess.pop('last_name', None)
    sess.pop('email', None)
    sess.pop('username', None)
    return c.RedirectResponse('/login', status_code=303)
