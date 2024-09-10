from fasthtml import common as c

def home_get(sess):
    access_token = sess.get('access_token')
    if not access_token:
        return c.RedirectResponse('/login', status_code=303)

    return c.Titled(
        "Home",
        c.Div(
            # Add a logout button
            c.A("Logout",
              href="/logout",
              cls="bg-red-500 text-white py-2 px-4 rounded mt-4",
              ),
            cls="flex justify-end"
        ),
    ) 
