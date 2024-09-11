from fasthtml import common as c
from components.header import Header
import requests

def home_get(sess):
    user = {
        "is_authenticated": True,
        "username": "JohnDoe",  # Example user details
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com"
    }
    access_token = sess.get('access_token')
    if not access_token:
        return c.RedirectResponse('/login', status_code=303)
    # headers = {
    #     "Authorization": f"Bearer {access_token}"
    # }
    # response = requests.get("http://localhost:8000/api/accounts/user/", headers=headers)

    return c.Div(
        Header(),
        c.Div(
        ),
        c.Div(
            # Add a logout button
            c.A("Logout",
              href="/logout",
              cls="bg-red-500 text-white py-2 px-4 rounded mt-4",
              ),
            cls="flex justify-end"
        ),
        cls="bg-gray-600 h-screen font-inter"
    ) 
