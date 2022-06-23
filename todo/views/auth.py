from flask import Blueprint, render_template, request, flash, redirect, url_for
from todo.forms import LoginForm, RegisterForm, SettingsForm
from todo.models import User
from todo import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email:
            if password:
                user_exists = User.query.filter_by(email=email).first()
                if user_exists:
                    if user_exists.password == password:
                        return redirect(url_for('fixed.home'))
                else:
                    flash("user doesnt exist")
            else:
                flash("password wont be empty")
        else:
            flash("email wont be empty")
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if first_name or last_name or email or password or confirm:
            user_exists = User.query.filter_by(email=email).first()
            if not user_exists:
                new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
            else:
                flash("user exists already.")
        else:
            flash("every area should be fill.")
    form = RegisterForm()
    return render_template('auth/register.html', form=form)


@auth.route('/settings')
def settings():
    form = SettingsForm()
    return render_template('auth/settings.html', form=form)
