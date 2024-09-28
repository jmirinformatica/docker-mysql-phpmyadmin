from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'), override=True)

class Config:
    FLASK_MYSQL_HOST = environ.get('FLASK_MYSQL_HOST')
    FLASK_MYSQL_PORT = int(environ.get('FLASK_MYSQL_PORT'))
    FLASK_MYSQL_USER = environ.get('FLASK_MYSQL_USER')
    FLASK_MYSQL_PASSWORD = environ.get('FLASK_MYSQL_PASSWORD')
    FLASK_MYSQL_DATABASE = environ.get('FLASK_MYSQL_DATABASE')
