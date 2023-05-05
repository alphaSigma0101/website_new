from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html'
    )


@app.route('/chat')
def chat_index():
    return render_template(
        'chat.html'
    )

@app.route('/employees')
def employees():
    return render_template(
        'employees.html'
    )

@app.route('/profile')
def profile():
    return render_template(
        'profile.html'
    )

@app.route('/add_task')
def add_task():
    return render_template(
        'add_task.html'
    )

if __name__ == '__main__':
    app.run(debug=True)
