from sqlalchemy import event
from sqlalchemy.sql import func

from todo import db


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    status = db.Column(db.String(8), nullable=False, default='idle')
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())
    expected_dead_line = db.Column(db.DateTime(timezone=True), nullable=False)
    ended_date = db.Column(db.DateTime(timezone=True))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task id:{self.id}>'


@event.listens_for(Task.__table__, 'after_create')
def insert_tasks(*args, **kwargs):
    from todo.create_data import create_tasks
    list_of_tasks = create_tasks()
    for task in list_of_tasks:
        db.session.add(task)
        db.session.commit()
