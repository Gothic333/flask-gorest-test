from flask import render_template, Blueprint

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def not_found_error(e):
    return render_template('errors/404.html', error=e), 404


@errors.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', error=e), 500
