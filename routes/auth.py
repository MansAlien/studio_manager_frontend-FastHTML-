from fasthtml.common import (
    dataclass,
    Form,
    Input,
    Button,
    Titled,
    RedirectResponse,
)
import requests

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

def login_post_route(login: LoginForm, sess):
    jwt_url = "http://localhost:8000/api/token/"
    payload = {'username': login.username, 'password': login.password}

    response = requests.post(jwt_url, json=payload)

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get("access")
        refresh_token = tokens.get("refresh")

        sess['access_token'] = access_token
        sess['refresh_token'] = refresh_token

        return RedirectResponse('/', status_code=303)
    else:
        return RedirectResponse('/login', status_code=303)

def logout_route(sess):
    sess.pop('access_token', None)
    sess.pop('refresh_token', None)
    return RedirectResponse('/login', status_code=303)
