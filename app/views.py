from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('task/tasks.html')


@app.route('/login')
def login():
    return render_template('auth/login.html')


@app.route('/register')
def register():
    return render_template('auth/register.html')


@app.route('/settings')
def settings():
    return render_template('auth/settings.html')


@app.route('/statics')
def statics():
    return render_template('task/statics.html')


@app.route('/about')
def about():
    return render_template('fixed/about.html')


@app.route('/create_new_task')
def create_new_task():
    return render_template('task/create_task.html')


@app.route('/get_detail')
def detail():
    return render_template('task/task.html')


if __name__ == '__main__':
    app.run()
