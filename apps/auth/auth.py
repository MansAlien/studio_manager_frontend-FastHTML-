import os
from datetime import datetime, timezone

import jwt
import requests
from dotenv import load_dotenv
from fasthtml import common as c
from fasthtml.common import dataclass

load_dotenv()
API_URL = os.getenv('API_URL')
LOGOUT_URL = f"{API_URL}logout/"
BLACKLIST_URL = f"{API_URL}accounts/blacklist/"
JWT_URL = f"{API_URL}token/"

def login_get_route(sess, error_message=None): # don't remove sess
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

    error_div = c.Div(
        c.P(error_message, cls="text-red-500 text-sm mt-2") if error_message else "",
        cls="text-center"
    )

    return c.Title("Sign In"), c.Div(
        c.Div(
            c.Div(
                frm, error_div,
                cls="sm:bg-gray-700 p-6 rounded-lg w-full max-w-sm"
            ),
            cls="flex h-full w-full justify-center items-center"
        ),
        cls="bg-gray-600 font-inter h-screen w-screen"
    )

@dataclass
class LoginForm:
    username: str
    password: str

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def login_post_route(login: LoginForm, sess):
    payload = {'username': login.username, 'password': login.password}

    response = requests.post(JWT_URL, json=payload)

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get("access")
        refresh_token = tokens.get("refresh")

        try:
            decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
        except jwt.InvalidTokenError:
            return login_get_route(sess, error_message="Invalid token received.")

        sess['access_token'] = access_token
        sess['refresh_token'] = refresh_token
        sess['username'] = decoded_token.get('username')
        sess['user_id'] = decoded_token.get('user_id')
        sess['first_name'] = decoded_token.get('first_name')
        sess['last_name'] = decoded_token.get('last_name')
        sess['email'] = decoded_token.get('email')
        sess['permissions'] = decoded_token.get('permissions')
        sess['is_superuser'] = decoded_token.get('is_superuser')

        return c.RedirectResponse('/', status_code=303)

    elif response.status_code == 401:
        return login_get_route(sess, error_message="Invalid username or password.")
    else:
        return login_get_route(sess, error_message="An error occurred. Please try again.")

def logout_blacklist(sess):
    sess.pop('access_token', None)
    sess.pop('refresh_token', None)
    sess.pop('first_name', None)
    sess.pop('last_name', None)
    sess.pop('email', None)
    sess.pop('username', None)
    sess.pop('user_id', None)
    sess.pop('permissions', None)
    sess.pop('is_superuser', None)
    return c.RedirectResponse('/login', status_code=303)

def logout_route(sess):
    # Remove the current user from the logged in users
    access_token = sess.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}
    requests.post(LOGOUT_URL, headers=headers)

    sess.pop('access_token', None)
    sess.pop('refresh_token', None)
    sess.pop('first_name', None)
    sess.pop('last_name', None)
    sess.pop('email', None)
    sess.pop('username', None)
    sess.pop('user_id', None)
    sess.pop('permissions', None)
    sess.pop('is_superuser', None)
    return c.RedirectResponse('/login', status_code=303)

def is_token_expired(access_token):
    try:
        decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
        exp_timestamp = decoded_token.get('exp')
        if not exp_timestamp:
            return True
        exp_time = datetime.fromtimestamp(exp_timestamp, timezone.utc)
        if exp_time < datetime.now(timezone.utc):
            return True
        return False
    except jwt.ExpiredSignatureError:
        return True
    except jwt.InvalidTokenError:
        return True

def is_blacklisted(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    blacklist_response = requests.get(BLACKLIST_URL, headers=headers)
    blacklist_data = blacklist_response.json()
    blocked = [True for block in blacklist_data if block["token"] == access_token]
    return blocked
