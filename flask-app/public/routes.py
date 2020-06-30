from flask import Blueprint, url_for, session, make_response, redirect
from functools import wraps
from database import db, models
import json

public = Blueprint('public', '__name__')

def login_required(f):
    # method wraps other functions
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'userName' in session: #if there is a user key in the session object, continue
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))
    return wrap

@public.route("/")
def index():
    res = make_response("Hello World")
    return res

@public.route("/test")
def test():
    branch = models.Branch.query.get(0)
    name = branch.name
    res = make_response(name)
    return res