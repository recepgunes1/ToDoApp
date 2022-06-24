from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class UpdateStatus(FlaskForm):
    status = SelectField(choices=['Idle', 'Complete', 'Give Up', 'Delete'])
    submit = SubmitField('Update')
