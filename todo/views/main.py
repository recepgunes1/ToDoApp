from operator import attrgetter

from flask import Blueprint, render_template
from flask_login import login_required, current_user

from todo.forms import UpdateStatus

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    list_of_tasks = list(filter(lambda t: t.status != 'deleted', current_user.tasks))
    list_of_tasks.sort(key=attrgetter('created_date'), reverse=True)
    update_status = UpdateStatus()
    return render_template('task/tasks.html', tasks=list_of_tasks, update_status=update_status)


@main.route('/about')
def about():
    return render_template('fixed/about.html')
