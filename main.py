from flask import Flask,jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATBASE_URL'] = 'postgresql://postgres:chantha@localhost:5432/Market'

db = SQLAlchemy(app)
class Product(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    barcode = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
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

@app.route('/market')
def market():
    items = [
        {'id':1001, 'name':"Phone", 'barcode':"10020334534", 'price':1000},
        {'id':1002, 'name':"Computer", 'barcode':"4520334534", 'price':500},
        {'id':1003, 'name':"Laptop", 'barcode':"100203545534", 'price':3000},
    ]
    return render_template('market.html', item_list=items)


if __name__ == '__main__':
    app.run('127.0.0.1', port=3001, debug=True)
