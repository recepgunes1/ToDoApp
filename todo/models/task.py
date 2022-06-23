from todo import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    status = db.Column(db.String(8), nullable=False)
    created_date = db.Column(db.Date(), nullable=False)
    expected_dead_line = db.Column(db.Date(), nullable=False)
    ended_date = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        return f'<Task id:{self.id}>'
