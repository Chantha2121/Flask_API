from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return '<h1>Hello</h1>'

@app.route('/admin')
def admin():
    return "This is admin!"

@app.route('/user/<name>')
def user(name):
    return render_template('User.html', user_name = name)


if __name__ == '__main__':
    app.run('127.0.0.1', port=3001, debug=True)
