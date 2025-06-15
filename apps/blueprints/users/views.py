from flask import Blueprint, redirect, render_template, request, url_for

from .forms import UsersForm
from .models import User
from .repository import UserRepository

users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
def index():
    page = request.args.get('page', default=1, type=int)
    return render_template('users/index.html',
                           users=UserRepository.get_all(page),
                           current_page=page,
                           page_count=UserRepository.get_page_count())


@users.route('/<int:user_id>', methods=['GET'])
def show_user(user_id):
    return render_template('users/user_detail.html',
                           user=UserRepository.get_by_id_or_404(user_id))


@users.route('/create', methods=['GET', "POST"])
def create_user():
    form = UsersForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        UserRepository.add_user(user)
        return redirect(url_for('users.index'))
    return render_template("users/user_create_page.html", form=form)


@users.route('/update/<int:user_id>', methods=['GET', "POST"])
def update_user(user_id):
    user = UserRepository.get_by_id_or_404(user_id)
    form = UsersForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        UserRepository.update_user(user)
        return redirect(url_for('users.index'))
    return render_template("users/user_update_page.html", form=form)


@users.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    UserRepository.delete_by_id(user_id)
    return redirect(url_for('users.index'))
