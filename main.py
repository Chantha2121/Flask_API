from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

@app.route('/admin')
def admin():
    return "This is admin!"

if __name__ == '__main__':
    app.run()