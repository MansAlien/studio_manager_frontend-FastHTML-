from fasthtml.common import (
    dataclass,
    Form,
    Input,
    Button,
    Titled,
    RedirectResponse,
)
import requests
import os
from dotenv import load_dotenv
import jwt

def login_get_route():
    frm = Form(
        Input(id='username', placeholder='Username'),
        Input(id='password', type='password', placeholder='Password'),
        Button('Login', type="submit"),
        action='/login', method='post'
    )
    return Titled("Login", frm)

@dataclass
class LoginForm:
    username: str
    password: str

# SECRET_KEY = "django-insecure-rvvd)ip@76fvqpak#c@#4ahe8=+aa3v==mcz=$ssj7*94_@@s*"
load_dotenv()
# SECRET_KEY = os.environ.get("SECRET_KEY")
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
            return RedirectResponse('/login', status_code=303)

        sess['access_token'] = access_token
        sess['refresh_token'] = refresh_token
        sess['username'] = login.username
        sess['user_id'] = user_id
        return RedirectResponse('/', status_code=303)
    else:
        return RedirectResponse('/login', status_code=303)

def logout_route(sess):
    sess.pop('access_token', None)
    sess.pop('refresh_token', None)
    sess.pop('username', None)
    sess.pop('user_id', None)
    return RedirectResponse('/login', status_code=303)
