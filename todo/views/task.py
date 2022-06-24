from flask import Blueprint, render_template, request, flash, abort, redirect, url_for
from flask_login import login_required, current_user

from todo import db
from todo.forms import CreateTaskForm
from todo.helpers import *
from todo.models import Task

task = Blueprint('task', __name__)


@task.route('/statics')
@login_required
def statics():
    return render_template('task/statics.html')


@task.route('/create', methods=['GET', 'POST'])
@login_required
def create_new_task():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        expected_dead_line = request.form.get('expected_dead_line')
        if title or content or expected_dead_line:
            new_task = Task(title=title, content=content, created_date=datetime.now(),
                            expected_dead_line=convert_to_date(expected_dead_line), owner_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('New task was added successfully.', 'success')
        else:
            flash('All inputs must be filled.', 'error')
    form = CreateTaskForm()
    return render_template('task/create_task.html', form=form)


@task.route('/detail/<int:tid>')
@login_required
def detail(tid: int):
    task_detail = Task.query.get(tid)
    if task_detail:
        if task_detail.owner_id == current_user.id:
            return render_template('task/task.html', task=task_detail)
        else:
            return "you cant access here"
    else:
        return abort(404)


@task.route('/update_status/<int:tid>', methods=['POST'])
@login_required
def update_status(tid: int):
    old_task = Task.query.get(tid)
    status = request.form.get('status')
    if status:
        if old_task.owner_id == current_user.id:
            old_task.status = status.lower()
            if old_task.status == 'complete':
                old_task.ended_date = datetime.now()
            db.session.commit()
            return redirect(url_for('fixed.home'))
