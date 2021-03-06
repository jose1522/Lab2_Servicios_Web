from os import environ
from dotenv import load_dotenv
from core.util import networking as net
load_dotenv()

class BaseConfig:
    SECRET_KEY = environ.get('SECRET_KEY')
    API_KEY = environ.get('API_KEY')
    WTF_CSRF_SECRET_KEY = environ.get('WTF_CSRF_SECRET_KEY')

    # SQLAlquemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class freeTDSConf(BaseConfig):
    SQLALQUEMY_DATABASE_URL_IP = net.getIP()
    SQLALQUEMY_DATABASE_URL_BASE = environ.get('SQLALQUEMY_DATABASE_URL_BASE') + SQLALQUEMY_DATABASE_URL_IP
    SQLALCHEMY_DATABASE_URI = SQLALQUEMY_DATABASE_URL_BASE + environ.get('SQLALQUEMY_DATABASE_URL_FREETDS')
    print(SQLALCHEMY_DATABASE_URI)

class msodbcConf(BaseConfig):
    SQLALQUEMY_DATABASE_URL_IP = environ.get("SQLALQUEMY_DATABASE_URL_IP")
    SQLALQUEMY_DATABASE_URL_BASE = environ.get('SQLALQUEMY_DATABASE_URL_BASE') + SQLALQUEMY_DATABASE_URL_IP
    SQLALCHEMY_DATABASE_URI = SQLALQUEMY_DATABASE_URL_BASE + environ.get('SQLALQUEMY_DATABASE_URL_MSODBC')
    print(SQLALCHEMY_DATABASE_URI)