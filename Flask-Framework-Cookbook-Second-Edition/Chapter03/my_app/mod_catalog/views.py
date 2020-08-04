# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

# first_or_404()
# get_or_404()
# paginate()


# ______________________________________________________________________


from flask import request, jsonify, Blueprint 
from my_app import db
from my_app.mod_catalog.models import Product
# ______________________________________________________________________

catalog = Blueprint('catalog', __name__, url_prefix='/catalog')
# ______________________________________________________________________


@catalog.route('/')
@catalog.route('/home/')
def home():
    return "Welcome to the Catalog Home."

# ______________________   

@catalog.route('/product/<id>/')
def product(id):
    product = Product.query.get_or_404(id)
    return 'Product - {} {}'.format(product.name,  product.price)

# ______________________  

@catalog.route('/products/')
def products():
    products = Product.query.all() 
    res = {} 
    
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price)
        }
    
    return jsonify(res)

# ______________________  

@catalog.route('/product-create', methods=['POST'])
def product_create():

    name = request.form.get('name')
    price = request.form.get('price')

    product = Product(name, price)

    db.session.add(product)
    db.session.commit()

    return 'Product created'