from flask import Flask
import datetime
from public.routes import public
from api.routes import api
from database import db
from .settings import *

def loadConf(OS):
    if OS == 'Darwin':
        return freeTDSConf()
    else:
        return msodbcConf()

def create_app(OS):
    app = Flask(__name__)
    app.config.from_object(loadConf(OS))
    app.permanent_session_lifetime = datetime.timedelta(days=1)

    # Register blueprints
    app.register_blueprint(public)
    app.register_blueprint(api, url_prefix='/api')

    # Instantiate SQLAlchemy
    db.init_app(app)

    return app