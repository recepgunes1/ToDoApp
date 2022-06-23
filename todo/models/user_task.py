# from todo.views import db
# from .user import *
# from .task import *
#
#
# class UserTask(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uid = db.Column(db.Integer, db.ForeignKey('user.id'))
#     tid = db.Column(db.Integer, db.ForeignKey('task.id'))
#
#     def __repr__(self):
#         return f'<UserTask {self.id}-{self.uid}-{self.tid}>'
