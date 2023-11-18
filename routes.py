from app import app
from flask import request
from auth import permission, route, get_paths

@app.errorhandler(405)
def method_not_allowed_error(error):
    return {"error": "Method Not Allowed"}, 405

@route("/some/<param>", {"GET": ["user"]})
def some(param, iam):
    """ 
        Description of this endpoint is added to 
        autodoc structure and can be presented later 
        in some help page
    """
    return {"some": param, "method": request.method, "role": iam}, 200

@route("/other/<param>", {"GET": ["user", "viewer"], "POST": ["user"]})
def func_with_desc(param, iam):
    """ Here goes another documented API endpoint """
    return {"some": param, "method": request.method, "role": iam}, 200

@route("/help", {"GET": ["anonymous"]})
def help():
    """ Help page is also documented as an API call """
    return get_paths(), 200

