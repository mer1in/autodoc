from flask import request
import inspect
from app import app

paths = {}

def permission(roles):
    def decorate(func):
        def wrapped(*args, **kwargs):
            inject_user_roles = "iam" in inspect.getfullargspec(func).args
            role = request.cookies.get("role", "anonymous")
            if (inject_user_roles):
                kwargs["iam"] = role
            if (role in roles or role=="admin" or "anonymous" in roles):
                return func(*args, **kwargs)
            return (
                {"error": f"""Forbidden method {request.method} for user {role}"""},
                403
            )
        wrapped.__name__ = func.__name__
        return wrapped
    return decorate

def route(path, methods):
    def decorate(func):
        global paths
        doc = func.__doc__
        paths[path] = {
            "description": doc,
            "permissions": methods
        }
        def run_with_permissions(*args, **kwargs):
            return permission(methods[request.method])(func)(*args, **kwargs)
        run_with_permissions.__name__ = func.__name__
        f = app.route(path, methods=list(methods.keys()))(run_with_permissions)
        return f
    return decorate

def get_paths():
    global paths
    return paths
