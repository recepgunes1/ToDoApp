import os
import secrets


class Config(object):
    ENV = 'Development'
    DEBUG = True
    SECRET_KEY = secrets.token_hex(16)
    DB_NAME = 'database.db'
    DB_PATH = os.getcwd()
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
