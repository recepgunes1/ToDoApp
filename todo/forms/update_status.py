from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class UpdateStatus(FlaskForm):
    status = SelectField(choices=[('idle', 'Idle'), ('complete', 'Complete'),
                                  ('give_up', 'Give Up'), ('delete', 'Delete')], coerce=str)
    submit = SubmitField('Update')
