from os import environ
from dotenv import load_dotenv
load_dotenv()

class BaseConfig:
    SECRET_KEY = environ.get('SECRET_KEY')
    API_KEY = environ.get('API_KEY')
    WTF_CSRF_SECRET_KEY = environ.get('WTF_CSRF_SECRET_KEY')

    # SQLAlquemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DarwinConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALQUEMY_DATABASE_URL_Mac')

class WindowsConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALQUEMY_DATABASE_URL')