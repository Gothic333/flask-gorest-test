from wtforms import (EmailField, IntegerField, RadioField, SelectField,
                     StringField, SubmitField)
from wtforms.validators import Email, InputRequired, Length, Optional

from apps.forms import BaseForm


class UsersForm(BaseForm):
    id = IntegerField('ID пользователя', [Optional()])
    name = StringField('ФИО пользователя', [InputRequired(), Length(min=5, max=255)])
    email = EmailField('Адрес электронной почты', [InputRequired(), Email()])
    gender = RadioField('Пол',
                        choices=[('male', 'Мужской'),
                                 ('female', 'Женский')],
                        validators=[InputRequired()], coerce=str)
    status = SelectField('Статус',
                         choices=[('active', 'Активен'),
                                  ('inactive', 'Неактивен')],
                         validators=[InputRequired()], coerce=str)
    submit = SubmitField('Отправить')
