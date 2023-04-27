from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


from data import db_session
from data.products import Product

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_session.global_init("db/shop.db")
db = SQLAlchemy(app)


@app.route('/')
def main():
    items = db_session.create_session().query(Product).all()
    return render_template('index.html', data=items)


@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/filter_1')
def filter_1():
    items_1 = db_session.create_session().query(Product).filter(Product.price < 2000)
    return render_template('filter_1.html', data=items_1)

@app.route('/filter_2')
def filter_2():
    items_2 = db_session.create_session().query(Product).filter(Product.price >= 2000, Product.price < 4000)
    return render_template('filter_2.html', data=items_2)

@app.route('/filter_3')
def filter_3():
    items_3 = db_session.create_session().query(Product).filter(Product.price >= 4000)
    return render_template('filter_3.html', data=items_3)
# @app.route('/new', methods=["POST", "GET"])
# def new():
#     if request.method == "POST":
#         name = request.form['name']
#         price = request.form['price']
#         about = request.form['about']
#
#         product_ = Product(name=name, price=price, about=about)
#         try:
#             db_session.create_session().add(product_)
#             db_session.create_session().commit()
#             return redirect('/')
#         except:
#             return "Произошла ошибка, неправильно введены данные"
#     else:
#         return render_template('new.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')


if __name__ == '__main__':
    app.run(debug=True)
