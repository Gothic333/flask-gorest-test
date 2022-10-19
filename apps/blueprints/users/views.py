from flask import render_template, Blueprint, url_for, redirect, flash, abort, request
from requests import HTTPError
from .forms import UsersForm
from .models import User
from .repository import UserRepository

users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
def index():
    page = request.args.get('page', default=1, type=int)
    users_page = UserRepository.get_all(page)
    if users_page is None:
        abort(404)
    page_count = UserRepository.get_page_count()
    return render_template('users/index.html', users=users_page, current_page=page, page_count=page_count)


@users.route('/<int:user_id>', methods=['GET'])
def show_user(user_id):
    user = UserRepository.get_by_id(user_id)
    if user is None:
        abort(404)
    return render_template('users/user_detail.html', user=user)


@users.route('/create', methods=['GET', "POST"])
def create_user():
    form = UsersForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        try:
            UserRepository.add_user(user)
            flash('Запись успешно добавлена', category='success')
        except HTTPError as e:
            flash(f'Ошибка: {e}', category='error')
        finally:
            return redirect(url_for('users.index'))
    return render_template("users/user_create_page.html", form=form)


@users.route('/update/<int:user_id>', methods=['GET', "POST"])
def update_user(user_id):
    user = UserRepository.get_by_id(user_id)
    if user is None:
        abort(404)
    form = UsersForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        try:
            UserRepository.update_user(user)
            flash('Запись успешно обновлена', category='success')
        except HTTPError as e:
            flash(f'Ошибка: {e}', category='error')
        finally:
            return redirect(url_for('users.index'))
    return render_template("users/user_update_page.html", form=form)


@users.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    try:
        UserRepository.delete_by_id(user_id)
        flash('Запись успешно удалена', category='success')
    except HTTPError as e:
        flash(f'Ошибка: {e}', category='error')
    finally:
        return redirect(url_for('users.index'))
