from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from todo import db
from todo.forms import LoginForm, RegisterForm, SettingsForm
from todo.helpers import *
from todo.models import User

auth = Blueprint('auth', __name__)


@auth.route('/sign_in', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.data.get('email').lower().strip() or None
        password = form.data.get('password') or None
        if email and password:
            user_exists = User.query.filter_by(email=email).first()
            if user_exists:
                if user_exists.password == create_md5(password):
                    login_user(user_exists, remember=True)
                    return redirect(url_for('main.home'))
                else:
                    flash('Password is wrong.', category='error')
            else:
                flash('User does not exist.', category='error')
        else:
            flash('All inputs must be filled.', category='error')
    return render_template('auth/login.html', form=form)


@auth.route('/sign_up', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        first_name = form.data.get('first_name').lower().strip() or None
        last_name = form.data.get('last_name').lower().strip() or None
        email = form.data.get('email').lower().strip() or None
        password = form.data.get('password') or None
        confirm = form.data.get('confirm') or None
        if first_name and last_name and email and password and confirm:
            if password == confirm:
                password_requirements = is_password_safe(password)
                if password_requirements[0]:
                    user_exists = User.query.filter_by(email=email).first()
                    if not user_exists:
                        new_user = User(first_name=first_name, last_name=last_name, email=email,
                                        password=create_md5(password))
                        db.session.add(new_user)
                        db.session.commit()
                        login_user(new_user, remember=True)
                        return redirect(url_for('main.home'))
                    else:
                        flash("User exists already.", category='error')
                else:
                    flash(password_requirements[1], category='error')
            else:
                flash("Passwords must match.", category='error')
        else:
            flash("All inputs must be filled.", category='error')
    return render_template('auth/register.html', form=form)


@auth.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm()
    if request.method == 'POST' and form.validate():
        flag = True
        first_name = form.data.get('first_name').lower().strip() or None
        last_name = form.data.get('last_name').lower().strip() or None
        email = form.data.get('email').lower().strip() or None
        new_password = form.data.get('new_password') or None
        confirm = form.data.get('confirm') or None
        current_password = form.data.get('current_password') or None
        if first_name and last_name and email and current_password:
            if current_user.password == create_md5(current_password):
                user = User.query.get(current_user.id)
                user.first_name = first_name
                user.last_name = last_name

                if current_user.email != email:
                    email_confirmation = User.query.filter_by(email=email).first()
                    if not email_confirmation:
                        user.email = email
                    else:
                        flash('you can\'t take this email.', category='error')
                        flag = False

                if new_password or confirm:
                    if new_password and confirm:
                        if new_password == confirm:
                            password_confirmation = is_password_safe(new_password)
                            if password_confirmation[0]:
                                user.password = create_md5(new_password)
                            else:
                                flash(password_confirmation[1], category='error')
                                flag = False
                        else:
                            flash('Passwords must match', category='error')
                            flag = False
                    else:
                        flash('All inputs must be filled.', category='error')
                        flag = False
                if flag:
                    db.session.commit()
                    flash('User was updated successfully.', category='success')
            else:
                flash('Current password is wrong.', category='error')
        else:
            flash('All inputs must be filled.', category='error')

    return render_template('auth/settings.html', form=form)


@auth.route('/sign_out', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
