from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    name = StringField(
        'Напишити имя выполняющего', validators=[DataRequired(message="Имя не может быть пустым!")]
    )
    task = TextAreaField(
        'Напишите текст задания', validators=[DataRequired(message="Задание не может быть пустым!")]
    )

    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    action = 'Авторизация'
    login = StringField(
        'Введите логин', validators=[DataRequired()]
    )
    password = PasswordField(
        'Введите пароль', validators=[DataRequired()]
    )
    submit = SubmitField('Войти')


class SignupForm(LoginForm):
    action = 'Регистрация'
    name = StringField(
        'Ваше имя', validators=[DataRequired()]
    )
    surname = StringField(
        'Ваша фамилия', validators=[DataRequired()]
    )
    birthday = StringField(
        'Дата рождения', validators=[DataRequired()]
    )
    submit = SubmitField('Зарегистрироваться')
