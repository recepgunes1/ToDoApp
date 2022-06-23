from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from todo.views import auth
    from todo.views import fixed
    from todo.views import task
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(fixed, url_prefix='/')
    app.register_blueprint(task, url_prefix='/')
    return app
