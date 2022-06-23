# from todo.views import db
#
#
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String, nullable=False)
#     last_name = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False, index=True, unique=True)
#     password = db.Column(db.String, nullable=False)
#
#     def __repr__(self):
#         return f'<User {self.id} {self.email}>'
