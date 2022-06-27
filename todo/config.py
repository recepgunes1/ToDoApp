import os
import secrets
from os import environ

import todo


class Config(object):
    ENV = environ.get('ENV') or environ.get('ENVIRONMENT') or 'Development'
    DEBUG = bool(environ.get('DEBUG')) or True
    SECRET_KEY = environ.get('SECRET_KEY') or secrets.token_hex(16)
    DB_NAME = environ.get('DB_NAME') or 'database.db'
    DB_PATH = environ.get('DB_PATH') or os.getcwd()
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APP_PATH = f'{os.getcwd()}/{todo.__name__}'
    STATIC_FOLDER = f'{APP_PATH}/static'
    INSERT_TEST_DATA = environ.get('INSERT_TEST_DATA') or True

    def __repr__(self):
        return f'<Config ENV={self.ENV} DEBUG={self.DEBUG} SECRET_KEY={self.SECRET_KEY} ' \
               f'DB_NAME={self.DB_NAME} DB_PATH={self.DB_PATH} INSERT_TEST_DATA={self.INSERT_TEST_DATA()}>'
