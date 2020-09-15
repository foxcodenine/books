# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

# first_or_404()
# get_or_404()
# paginate()

# ______________________________________________________________________


from flask import render_template, request, jsonify, Blueprint
from my_app import db 
from my_app.mod_catalog.database import Product, Category 

from my_app import redis

from flask_cors import CORS, cross_origin

# ______________________________________________________________________


catalog = Blueprint('catalog', __name__, url_prefix='/catalog')
# ______________________________________________________________________
# GET ROUTES


# @catalog.route('/')
# @catalog.route('/home/')
# def home():
#     return "Welcom to the Catalog Homepage!"

@catalog.route('/')
@catalog.route('/home/')
def home():


    request_xhr_key = request.headers.get('X-Requested-With')

    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':

        products = Product.query.all()

        return jsonify({
                'count': len(products)})

    

    
    return render_template('home.html')


# ______________________ 

# @catalog.route('/product/<id>/')
# def product(id):
#     # get_or_404 will return an instance based on the given primary key
#     # or will raise 404 errors instead of returning None
#     product = Product.query.get_or_404(id)

#     # Saveing the visited items to redis
#     product_key = 'product-{}'.format(product.id)
#     redis.set(product_key, product.name)
#     redis.expire(product_key, 600)

#     return 'Product - {} <br> Price - {}'.format(product.name,  product.price)

@catalog.route('product/<id>/')
def product(id):
    product = Product.query.get_or_404(id)

    # Saveing the visited items to redis
    product_key = 'product-{}'.format(product.id)
    redis.set(product_key, product.name)
    redis.expire(product_key, 600)

    return render_template('product.html', product=product)



# ______________________ 

# @catalog.route('/products/<int:page>')
# def products(page):

#     # products = Product.query.all()

#     # Adding pagination in the search query
#     products = Product.query.paginate(page, 3, error_out=False).items

#     res = {}

#     for product in products:
#         res[product.id] = {
#             'name': product.name, 
#             'price': str(product.price),
#             'category': product.category.name
#         }
#     return jsonify(res)

@catalog.route('/products/')
@catalog.route('/products/<int:page>/')
def products(page=1):

    request_xhr_key = request.headers.get('X-Requested-With')

    # Products API_______
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        
        products = Product.query.all()
        
        res = {} 
    
        for product in products:
            res[product.id] = {
                'name': product.name,
                'price': str(product.price),
                'category': product.category.name
            }

        return jsonify(res)
        # API END________
        
    products = Product.query.paginate(page, 4)
    return render_template('products.html', products=products)





    
    
# ______________________ 

@catalog.route('/category/<id>')
def category(id):
    current_category = Category.query.get_or_404(id)
    return render_template('category.html', catagory=current_category)
# ______________________ 

# @catalog.route('/categories')
# def categories():
#     categories = Category.query.all() 
#     res = {}

#     for category in categories:
#         res[category.id] = {'name': category.name}
      

#         res[category.id]['products'] = {}

#         for product in category.products:
#             res[category.id]['products'][product.id] = {
#                     'id': product.id,
#                     'name':product.name,
#                     'price': str(product.price) 
#                 }
    
#     return jsonify(res)

@catalog.route('/categories')
def categories():
    categories = Category.query.all()

    return render_template('categories.html', categories=categories)

# ______________________ 
@catalog.route('/recent-products')
def recent_products():
    # In this line we get all the keys
    keys_alive = redis.keys('product-*')

    # And here we use a List Comprehensions to make a list with the product-names
    products = [redis.get(k).decode('utf-8') for k in keys_alive]

    return jsonify({'products': products})


# ______________________________________________________________________
# POST ROUTES

@catalog.route('/product-create', methods=['POST'])
def product_create():

    name = request.form.get('name')
    price = request.form.get('price')
    categ_name = request.form.get('category')

    category = Category.query.filter_by(name=categ_name).first()
    
    if not category:
        category = Category(categ_name)

    product = Product(name, price, category)

    db.session.add(product)
    db.session.commit()

    return 'Product created'

'''

>> python

import requests

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'Ocean 39 GMT premium 500 Ceramic', 'price': '690', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'Sinn 556 A RS', 'price': '1190', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'CITIZEN Promaster Diver 200', 'price': 189.99', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'TISSOT PRS 516 Automatic', 'price': '325', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'TAG HEUER Formula 1', 'price': '1049', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'INVICTA Mako Pro Diver Automatic', 'price': '84.99', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'LONGINES HydroConquest Automatic', 'price': '865', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'HAMILTON Timeless Classic Automatic Silver Dial', 'price': '575', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'CASIO G-Shock Black Resin Strap', 'price': '63.50', 'category': 'watch'})
'''

# ______________________  

@catalog.route('/category-create', methods=['POST'])
def crete_category():
    name = request.form.get('name')
    

    category = Category.query.filter_by(name=name).first()

    if not category:
        category = Category(name)



    db.session.add(category)
    db.session.commit()

    return 'Categort created'