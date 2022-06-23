from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired


class CreateTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    expected_dead_line = DateField('Expected Dead Line', validators=[DataRequired()])
    submit = SubmitField('Save It')
