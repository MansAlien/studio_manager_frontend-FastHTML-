from fasthtml.common import Button


def button(label, color="default", hx_get=None, hx_post=None, hx_swap=None, hx_target=None, extra={}):
    styles = {
        "default": "text-white bg-blue-600 hover:bg-blue-700 focus:ring-blue-800",
        "alternative": "text-gray-400 bg-gray-800 border border-gray-600 hover:text-white hover:bg-gray-700",
        "dark": "text-white bg-gray-800 hover:bg-gray-700 focus:ring-gray-700 border-gray-700",
        "light": "text-white bg-gray-800 border border-gray-600 hover:bg-gray-700 hover:border-gray-600 focus:ring-gray-700",
        "green": "text-white bg-green-600 hover:bg-green-700 focus:ring-green-800",
        "red": "text-white bg-red-600 hover:bg-red-700 focus:ring-red-900",
        "yellow": "text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-yellow-900",
        "purple": "text-white bg-purple-600 hover:bg-purple-700 focus:ring-purple-900",
        "tab_active": """ 
            py-2 m-0 rounded-lg text-white rounded-b-none
            shadow-none bg-transparent bg-gray-500 hover:bg-gray-500 border-none
            """,
        "tab" : """ 
            px-4 py-2 m-0 rounded-lg text-white rounded-b-none
            shadow-none bg-transparent hover:bg-gray-500 border-none 
            """
    }
    attrs = {
        "cls": f"{styles[color]} focus:outline-none font-medium rounded-lg text-base px-5 py-2.5 me-2 mb-2 border-transparent",
    }
    
    if hx_get:
        attrs["hx-get"] = hx_get
    if hx_post:
        attrs["hx-post"] = hx_post
    if hx_swap:
        attrs["hx-swap"] = hx_swap
    if hx_target:
        attrs["hx-target"] = hx_target
    if color == "tab" :
        attrs["cls"] = styles["tab"]
        attrs["_"] =  "on click remove .bg-gray-500 from <button/> in tabs then add .bg-gray-500 on me"
    if color == "tab_active":
        attrs["cls"] = styles["tab_active"]
        attrs["_"] =  "on click remove .bg-gray-500 from <button/> in tabs then add .bg-gray-500 on me"

    return  Button(
        label,
        type="button",
        **attrs,
        **extra
    )
