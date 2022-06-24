from flask import Blueprint, render_template
from flask_login import login_required, current_user

from todo.models import Task
from todo.forms import UpdateStatus

fixed = Blueprint('fixed', __name__)


@fixed.route('/', methods=['GET', 'POST'])
@fixed.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    list_of_tasks = list(current_user.tasks)
    update_status = UpdateStatus()
    return render_template('task/tasks.html', tasks=list_of_tasks, update_status=update_status)


@fixed.route('/about')
def about():
    return render_template('fixed/about.html')
