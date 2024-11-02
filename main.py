from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    items = [
        {'id':1001, 'name':"Phone", 'barcode':"10020334534", 'price':1000},
        {'id':1002, 'name':"Computer", 'barcode':"4520334534", 'price':500},
        {'id':1003, 'name':"Laptop", 'barcode':"100203545534", 'price':3000},
    ]
    return render_template('index.html', item_list = items)

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
