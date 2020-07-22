from flask import Flask 
from my_app.mod.views import hello
from my_app.mod_product.views import product_blueprint



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

import my_app.mod.views
import my_app.mod_product.views