from flask import Blueprint, render_template

fixed = Blueprint('fixed', __name__)


@fixed.route('/')
@fixed.route('/home')
def home():
    return render_template('task/tasks.html')


@fixed.route('/about')
def about():
    return render_template('fixed/about.html')
