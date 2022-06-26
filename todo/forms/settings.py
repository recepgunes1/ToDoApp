from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired


class SettingsForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('E-Mail', validators=[DataRequired()])
    new_password = PasswordField('Password', validators=[])
    confirm = PasswordField('Password (Validate)', validators=[])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    submit = SubmitField('Save It')
