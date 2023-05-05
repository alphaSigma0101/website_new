from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    task_text = db.Column(db.Text)
    deadline = db.Column(db.DateTime)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    birthday = db.Column(db.DateTime)
    family_status = db.Column(db.DateTime)
    education = db.Column(db.String(255))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.Integer)
    direction = db.Column(db.Integer)
    people = db.relationship('Profile', backref='staff')


db.create_all()


class TaskForm(FlaskForm):
    name = StringField(
        'Напишити имя выполняющего', validators=[DataRequired(message="Имя не может быть пустым!")]
    )
    task = TextAreaField(
        'Напишите текст задания', validators=[DataRequired(message="Задание не может быть пустым!")]
    )

    submit = SubmitField('Добавить')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html'
    )


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template(
        'chat.html'
    )


@app.route('/employees', methods=['GET', 'POST'])
def employees():
    return render_template(
        'employees.html'
    )


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template(
        'profile.html'
    )


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    now = datetime.now().strftime("%d.%m.%Y")
    if form.validate_on_submit():
        try:
            task = Task()
            task.name = form.name.data
            task.task_text = form.task.data
            task.deadline = datetime.strptime(now, "%d.%m.%Y")
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception:
            return redirect(url_for('index'))
    return render_template(
        'add_task.html', form=form
    )


if __name__ == '__main__':
    app.run(debug=True)
