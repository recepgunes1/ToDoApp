import os
import secrets

import todo


class Config(object):
    ENV = 'Development'
    DEBUG = True
    SECRET_KEY = secrets.token_hex(16)
    DB_NAME = 'database.db'
    DB_PATH = os.getcwd()
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APP_PATH = f'{os.getcwd()}/{todo.__name__}'
    STATIC_FOLDER = f'{APP_PATH}/static'
    INSERT_TEST_DATA = True
