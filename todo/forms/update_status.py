from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class UpdateStatus(FlaskForm):
    status = SelectField(choices=[('idle', 'Idle'), ('completed', 'Complete'),
                                  ('gave_up', 'Give Up'), ('deleted', 'Delete')])
    submit = SubmitField('Update')
