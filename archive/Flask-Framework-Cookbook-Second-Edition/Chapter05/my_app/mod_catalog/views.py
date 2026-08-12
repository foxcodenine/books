# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

# first_or_404()
# get_or_404()
# paginate()

# ______________________________________________________________________


from flask import render_template, request, jsonify, Blueprint, url_for, flash, redirect
from my_app import db 
from my_app.mod_catalog.database import Product, Category 

from my_app import redis, app

from flask_cors import CORS, cross_origin

from flask import make_response, send_from_directory
from werkzeug.exceptions import HTTPException
import os 

from my_app.mod_catalog.forms import ProductForm

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

# Chapter3 route - Superseded
@catalog.route('/_c3/product-create', methods=['POST'])
def product_create_c3():
    # this is the old router (_r)
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

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'Ocean 39 GMT premium 500 Ceramic', 'price': '690', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'Sinn 556 A RS', 'price': '1190', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'CITIZEN Promaster Diver 200', 'price': 189.99', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'TISSOT PRS 516 Automatic', 'price': '325', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'TAG HEUER Formula 1', 'price': '1049', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'INVICTA Mako Pro Diver Automatic', 'price': '84.99', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'LONGINES HydroConquest Automatic', 'price': '865', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'HAMILTON Timeless Classic Automatic Silver Dial', 'price': '575', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/_r/product-create',
data={'name': 'CASIO G-Shock Black Resin Strap', 'price': '63.50', 'category': 'watch'})
'''
# _____________________________

# Chapter4 route - Superseded
@catalog.route('/_c4/product-create', methods=['GET', 'POST'])
def product_create_c4():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        categ_name = request.form.get('category')   

        print('>>', name, price, categ_name)    

        # Check if category already in db
        # If not it will be created

        category = Category.query.filter_by(name=categ_name).first()

        if not category:
            category = Category(name=categ_name)    
        
        # Check if product already in db
        # If not it will be created

        product = Product.query.filter_by(name=name).first()

        if product:
            flash('The product {} has already been created!'.format(name), 'danger')
            return redirect(url_for('catalog.product', id=product.id))
        else:
            product = Product(
                name=name, price=price, category=category
            )
            db.session.add(product)
            db.session.commit()
            flash('The product {} has been created'.format(name), 'success')

            return redirect(url_for('catalog.product', id=product.id))
    return render_template('product-create-c4.html')
# _____________________________

@catalog.route('/product-create', methods=['GET', 'POST'])
def product_create():


    form = ProductForm(csrf_enabled=False)

    # In the following code:

    # In the 1st line we are fetching the categories from db and after
    # setting categories as a list of tuple with the id and name of all
    # the categories. 
    
    # In the 2nd line we are setting the categories list to choices for the
    # category field to be displayed as options in the selection input.

    categories = [(c.id, c.name) for c in Category.query.all()] #<- 1st line
    form.category.choices = categories #<- 2nd line

    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
         
        # form.category.data will return the id which is the primay key
        # in the category field (db)

        # get_or_404 will return an instance based on the given primary key
        # or will raise 404 errors instead of returning None
        category = Category.query.get_or_404(form.category.data)

        print('>>', name, price, category)         

        
        # Check if product already in db
        # If not it will be created

        product = Product.query.filter_by(name=name).first()

        if product:
            flash('The product {} has already been created!'.format(name), 'danger')
            return redirect(url_for('catalog.product', id=product.id))
        else:
            product = Product(
                name=name, price=price, category=category
            )
            db.session.add(product)
            db.session.commit()
            flash('The product {} has been created'.format(name), 'success')

            return redirect(url_for('catalog.product', id=product.id, form=form))
    return render_template('product-create.html', form=form)

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

# ______________________________________________________________________  
# Error handiling:
# This will render a template for an 404 error .

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# ______________________  

# Or this will accept all error, it is set to return a json as body 
# and has a header.

@app.errorhandler(HTTPException)
def http_error_handler(e):

    error_body = jsonify({
        'code': e.code,
        'name': e.name,
        'description': e.description
    })

    response = make_response(
        error_body,
        e.code
    )
    response.headers['Content-Type'] = 'application/json'
    response.headers['Code'] = e.code
    response.headers['Error'] = e.name
    response.headers['Description'] = e.description
   
    # return response

    # or here is set to return a template
    return render_template(
        'error.html', 
        code=e.code ,
        name=e.name,
        description=e.description
    )
# ______________________________________________________________________ 
# coffee_tree_leafs_icon.svg

# Adding a favicon

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
                os.path.join(app.root_path, 'static/icon'),
                'coffee_tree_leafs_icon.ico',
                mimetype='image/vnd.microsoft.icon'
    )

# ______________________________________________________________________
# Search Route

@catalog.route('product-search', methods=['GET', 'POST'])
@catalog.route('product-search/<int:page>', methods=['GET', 'POST'])
def product_search(page=1):

    if request.method == 'GET':
        return render_template('product-search.html')

    if request.method == 'POST':

        products = Product.query

        # ___create filters___
        
        if request.form['name']:
            name = request.form['name']
            
            products = products.filter(Product.name.like('%' + name + '%'))
            print(products.all())
        
        if request.form['price-min'] or request.form['price-max']:

            price_min = int(request.form['price-min'])
            price_max = int(request.form['price-max'])
            
            print('>>>', price_min, price_max)
            if not price_min : price_min = 0
            if not price_max : price_max = 999999

            products = products.filter(Product.price >= price_min).filter(Product.price <= price_max)

        if request.form['category']:
            category = request.form['category']

            category_id = Category.query.filter_by(name = category).first().id

            products = products.filter(Product.category_id == category_id)

        # ___end filters___

        return render_template(
            'products.html', products=products.paginate(page, 10)
        )
# ______________________________________________________________________