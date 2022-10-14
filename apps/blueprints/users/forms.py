from wtforms import EmailField, StringField, IntegerField, RadioField, SelectField, SubmitField
from wtforms.validators import InputRequired, Optional, Length, Email
from apps.forms import BaseForm
from .enums import GenderEnum, StatusEnum


class UsersForm(BaseForm):
    id = IntegerField('ID пользователя', [Optional()])
    name = StringField('ФИО пользователя', [InputRequired(), Length(min=5, max=255)])
    email = EmailField('Адрес электронной почты', [InputRequired(), Email(granular_message=True)])
    gender = RadioField('Пол',
                        choices=[(GenderEnum.MALE.value, 'Мужской'),
                                 (GenderEnum.FEMALE.value, 'Женский')],
                        validators=[InputRequired()], coerce=str)
    status = SelectField('Статус',
                         choices=[[(StatusEnum.ACTIVE.value, 'Активен'),
                                   (StatusEnum.INACTIVE.value, 'Неактивен')]],
                         validators=[InputRequired()], coerce=str)
    submit = SubmitField('Отправить')
