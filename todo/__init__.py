from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from todo.views import auth
    from todo.views import fixed
    from todo.views import task

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(fixed, url_prefix='/')
    app.register_blueprint(task, url_prefix='/')

    from todo.models import User
    from todo.models import Task
    from todo.models import UserTask

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
        db.create_all(app=app)
