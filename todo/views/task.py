from flask import Blueprint, render_template, request, flash, abort, url_for, redirect
from flask_login import login_required, current_user

from todo import db
from todo.forms import CreateTaskForm, UpdateStatus
from todo.helpers import *
from todo.models import Task

task = Blueprint('task', __name__)


@task.route('/statics')
@login_required
def statics():
    flag = False
    statics_of_tasks = {'idle': len(list(filter(lambda t: t.status == 'idle', current_user.tasks))),
                        'completed': len(list(filter(lambda t: t.status == 'completed', current_user.tasks))),
                        'deleted': len(list(filter(lambda t: t.status == 'deleted', current_user.tasks))),
                        'gave_up': len(list(filter(lambda t: t.status == 'gave_up', current_user.tasks)))
                        }
    if True in [s > 0 for s in statics_of_tasks.values()]:
        draw_plot(statics_of_tasks, current_user.id)
        flag = True
    return render_template('task/statics.html', statics=statics_of_tasks, flag=flag)


@task.route('/create', methods=['GET', 'POST'])
@login_required
def create_new_task():
    form = CreateTaskForm()
    if request.method == 'POST' and form.validate():
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
    return render_template('task/create_task.html', form=form)


@task.route('/detail/<int:tid>')
@login_required
def detail(tid: int):
    task_detail = Task.query.get(tid)
    if task_detail:
        if task_detail.owner_id == current_user.id:
            form = UpdateStatus()
            form.status.default = task_detail.status
            form.process()
            return render_template('task/task.html', task=task_detail, form=form)
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
            old_task.status = status
            if old_task.status == 'completed':
                old_task.ended_date = datetime.now()
            db.session.commit()
            return redirect(url_for('main.home'))
