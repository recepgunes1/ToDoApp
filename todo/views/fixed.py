from flask import Blueprint, render_template

from todo.models import Task

fixed = Blueprint('fixed', __name__)


@fixed.route('/', methods=['GET', 'POST'])
@fixed.route('/home', methods=['GET', 'POST'])
def home():
    list_of_tasks = list(Task.query.all())
    return render_template('task/tasks.html', tasks=list_of_tasks)


@fixed.route('/about')
def about():
    return render_template('fixed/about.html')
