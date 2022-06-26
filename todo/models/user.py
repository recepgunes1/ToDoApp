from flask_login import UserMixin
from sqlalchemy import event
from sqlalchemy.sql import func

from todo import db
from todo.config import Config


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())
    tasks = db.relationship('Task', backref='user', passive_deletes=True)

    def __repr__(self):
        return f'<User id:{self.id}>'


if Config.INSERT_TEST_DATA:
    @event.listens_for(User.__table__, 'after_create')
    def insert_tasks(*args, **kwargs):
        from todo.create_data import create_users
        list_of_users = create_users()
        for user in list_of_users:
            db.session.add(user)
            db.session.commit()
