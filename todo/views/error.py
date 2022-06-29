from flask import Blueprint, render_template

error = Blueprint('error', __name__)


@error.app_errorhandler(Exception)
def handler(e):
    data = {'error_title': str(e).split(':')[0],
            'error_content': str(e).split(':')[1]}
    return render_template('error.html', **data)
