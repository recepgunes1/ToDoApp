import os
import secrets
from distutils.util import strtobool
from os import environ

import todo


class Config(object):
    ENV = environ.get('ENV') or environ.get('ENVIRONMENT') or 'Development'
    DEBUG = bool(strtobool(environ.get('DEBUG', 'True')))
    SECRET_KEY = environ.get('SECRET_KEY') or secrets.token_hex(16)
    DB_NAME = environ.get('DB_NAME') or 'database.db'
    DB_PATH = environ.get('DB_PATH') or os.getcwd()
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(strtobool(environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'True')))
    STATIC_FOLDER = f'{os.getcwd()}/{todo.__name__}/static'
    INSERT_TEST_DATA = bool(strtobool(environ.get('INSERT_TEST_DATA', 'True')))

    def __repr__(self):
        return f'<Config ENV={self.ENV} DEBUG={self.DEBUG} SECRET_KEY={self.SECRET_KEY} ' \
               f'DB_NAME={self.DB_NAME} DB_PATH={self.DB_PATH} INSERT_TEST_DATA={self.INSERT_TEST_DATA}>'
