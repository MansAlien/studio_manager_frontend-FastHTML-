from fasthtml.common import Titled, P

def home_get():
    return Titled("FastHTML", P("Let's do this!", cls="text-red-5")) 
