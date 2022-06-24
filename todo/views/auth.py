from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

from todo import db
from todo.forms import LoginForm, RegisterForm, SettingsForm
from todo.helpers import *
from todo.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = request.form.get('email')
        password = request.form.get('password')
        if email or password:
            user_exists = User.query.filter_by(email=email).first()
            if user_exists:
                if user_exists.password == create_md5(password):
                    login_user(user_exists, remember=True)
                    return redirect(url_for('fixed.home'))
                else:
                    flash('Password is wrong.', category='error')
            else:
                flash('User does not exist.', category='error')
        else:
            flash('All inputs must be filled.', category='error')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if first_name or last_name or email or password or confirm:
            if password == confirm:
                user_exists = User.query.filter_by(email=email).first()
                if not user_exists:
                    new_user = User(first_name=first_name, last_name=last_name, email=email,
                                    password=create_md5(password))
                    db.session.add(new_user)
                    db.session.commit()
                    login_user(new_user, remember=True)
                    return redirect(url_for('fixed.home'))
                else:
                    flash("User exists already.", category='error')
            else:
                flash("Passwords must match.", category='error')
        else:
            flash("All inputs must be filled.", category='error')
    return render_template('auth/register.html', form=form)


@auth.route('/settings')
@login_required
def settings():
    form = SettingsForm()
    return render_template('auth/settings.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('fixed.home'))
