# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

# first_or_404()
# get_or_404()
# paginate()


# ______________________________________________________________________


from flask import request, jsonify, Blueprint 
from my_app import db
from my_app.mod_catalog.models import Product, Category
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
    return 'Product - {} <br> Price - {}'.format(product.name,  product.price)

# ______________________  

@catalog.route('/products/')
def products():
    products = Product.query.all() 
    res = {} 
    
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price),
            'category': product.category.name
        }
    
    return jsonify(res)

# ______________________  

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



# ______________________  

@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    res = {} 

    for category in categories:
        res[category.id] = {'name': category.name}

        res[category.id]['products'] = {}

        for product in category.products:
            res[category.id]['products'][product.id] = {
                    'id': product.id,
                    'name':product.name,
                    'price': str(product.price) 
                }
    
    return jsonify(res)
