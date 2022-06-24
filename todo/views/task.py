from flask import Blueprint, render_template, request, flash

from todo import db
from todo.forms import CreateTaskForm
from todo.helpers import *
from todo.models import Task

task = Blueprint('task', __name__)


@task.route('/statics')
def statics():
    return render_template('task/statics.html')


@task.route('/create', methods=['GET', 'POST'])
def create_new_task():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        expected_dead_line = request.form.get('expected_dead_line')
        if title or content or expected_dead_line:
            new_task = Task(title=title, content=content, created_date=datetime.now(),
                            expected_dead_line=convert_to_date(expected_dead_line))
            db.session.add(new_task)
            db.session.commit()
            flash('New task was added successfully.', 'success')
        else:
            flash('All inputs must be filled.', 'error')
    form = CreateTaskForm()
    return render_template('task/create_task.html', form=form)


@task.route('/detail/<int:tid>')
def detail(tid: int):
    task_detail = Task.query.get(tid)
    if task_detail:
        return render_template('task/task.html', task=task_detail)


@task.route('/complete/<int:tid>')
def complete(tid: int):
    task_detail = Task.query.get(tid)
    if task_detail:
        return render_template('task/task.html', task=task_detail)


@task.route('/gave_up/<int:tid>')
def gave_up(tid: int):
    task_detail = Task.query.get(tid)
    if task_detail:
        return render_template('task/task.html', task=task_detail)


@task.route('/delete/<int:tid>')
def delete(tid: int):
    task_detail = Task.query.get(tid)
    if task_detail:
        return render_template('task/task.html', task=task_detail)
