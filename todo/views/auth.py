from flask import Blueprint, render_template
from todo.forms import LoginForm, RegisterForm, SettingsForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)


@auth.route('/settings')
def settings():
    form = SettingsForm()
    return render_template('auth/settings.html', form=form)
