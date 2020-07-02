from flask import Flask
import datetime
from public.routes import public
from database import db, ma
from .settings import *
from flask_bootstrap import Bootstrap

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

    # Instantiate SQLAlchemy
    db.init_app(app)
    ma.init_app(app)

    Bootstrap(app)

    return app