from flask import Blueprint, url_for, session, make_response, redirect
from functools import wraps
from database import db, models
from core.util import networking as net
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
    canton = models.Canton.query.get(1)
    name = canton.Nombre
    res = make_response("{0}, {1}".format(name,net.getIP()))
    return res

@public.route("/myip")
def myIP():
    res = make_response(net.getIP()+"/"+net.getGatewayIP())
    return res