from flask_login import UserMixin
from sqlalchemy.sql import func

from todo import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())
    tasks = db.relationship('Task', backref='user', passive_deletes=True)

    def __repr__(self):
        return f'<User id:{self.id}>'
