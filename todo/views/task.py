from flask import Blueprint, render_template
from todo.forms import CreateTaskForm

task = Blueprint('task', __name__)


@task.route('/statics')
def statics():
    return render_template('task/statics.html')


@task.route('/create_new_task', methods=['GET', 'POST'])
def create_new_task():
    form = CreateTaskForm()
    return render_template('task/create_task.html', form=form)


@task.route('/get_detail')
def detail():
    return render_template('task/task.html')
