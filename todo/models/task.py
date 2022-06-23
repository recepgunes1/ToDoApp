# from todo.views import db
#
#
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     content = db.Column(db.String, nullable=False)
#     created_date = db.Column(db.Date, nullable=False)
#     expected_dead_line = db.Column(db.Date, nullable=False)
#     dead_line = db.Column(db.Date, nullable=False)
#
#     def __repr__(self):
#         return f'<Task {self.id} {self.title}>'
