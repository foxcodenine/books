
from flask import render_template, Blueprint
from my_app.mod_product.models import PRODUCTS
from werkzeug.exceptions import abort

# ______________________________________________________________________

product_blueprint = Blueprint('product', __name__, url_prefix='/product')

# ______________________________________________________________________


@product_blueprint.route('/')
@product_blueprint.route('/home/')
def home():
    return render_template('home.html', products = PRODUCTS)

# _______________________


@product_blueprint.route('/<key>/')
def product(key):
    product = PRODUCTS.get(key)
    if not product_blueprint:
        abort(404)
    render_template('product.html', product=product)

# _______________________