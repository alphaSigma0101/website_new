from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
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


if __name__ == '__main__':
    app.run(debug=True)
