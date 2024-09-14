from fasthtml.common import dataclass
from fasthtml import common as c
import requests
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timezone

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
    return c.Title("Studio Vision"), c.Div(
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
        except jwt.InvalidTokenError:
            return c.RedirectResponse('/login', status_code=303)

        # Extract and save user information in the session
        sess['access_token'] = access_token
        sess['refresh_token'] = refresh_token
        sess['username'] = decoded_token.get('username')
        sess['first_name'] = decoded_token.get('first_name')
        sess['last_name'] = decoded_token.get('last_name')
        sess['email'] = decoded_token.get('email')

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

#check if the access token is expired
def is_token_expired(access_token):
    try:
        decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
        exp_timestamp = decoded_token.get('exp')
        if not exp_timestamp:
            return True  # If no 'exp' claim, consider the token expired
        exp_time = datetime.fromtimestamp(exp_timestamp, timezone.utc)
        if exp_time < datetime.now(timezone.utc):
            return True  # Token is expired
        return False  # Token is valid
    except jwt.ExpiredSignatureError:
        return True  # Token has already expired
    except jwt.InvalidTokenError:
        return True  # Token is invalid or malformed
