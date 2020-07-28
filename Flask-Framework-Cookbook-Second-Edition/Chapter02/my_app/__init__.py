from flask import Flask, request
from my_app.mod.views import hello
from my_app.mod_product.views import product_blueprint

import ccy



# ______________________________________________________________________

app = Flask(__name__)

if app.config['ENV'] == 'development':
    app.config.from_object('config.ConfigDev')
else:
    app.config.from_object('config.ConfigPro')


app.register_blueprint(hello)
app.register_blueprint(product_blueprint)
# ______________________________________________________________________


@app.route('/')
def index():
    return '{}'.format(app.config['CHECK_ENV'])

# ______________________________________________________________________

# If the filter is at the blueprint level, the decorator would be app_template_filter ;
# otherwise, at the application level, the decorator would be template_filter;

@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return '{} {}'.format(currency_code, amount)


# ______________________________________________________________________

import my_app.mod.views
import my_app.mod_product.views