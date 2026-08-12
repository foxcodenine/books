
from flask import render_template, Blueprint, request
from my_app.mod_product.models import PRODUCTS
from werkzeug.exceptions import abort

# ______________________________________________________________________

product_blueprint = Blueprint('product', __name__, url_prefix='/products')

# ______________________________________________________________________


@product_blueprint.route('/')
@product_blueprint.route('/home/')
def home():
    # This will get the best match client language according location 
    print('>>>>>', request.accept_languages.best)

    return render_template('home.html', products = PRODUCTS)

# _______________________


@product_blueprint.route('/<key>/')
def product(key):
    product = PRODUCTS.get(key)
    if not product_blueprint:
        abort(404)
    return render_template('product.html', product=product)


# _______________________

# Create Filter at blueprint level

# If the filter is at the blueprint level, the decorator would be app_template_filter ;
# otherwise, at the application level, the decorator would be template_filter;

@product_blueprint.app_template_filter('full_name')
def full_name_filter(product):
    return '{0} / {1}'.format(product['category'], product['name'])
