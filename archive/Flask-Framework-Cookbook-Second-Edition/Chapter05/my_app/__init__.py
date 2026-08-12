from flask import Flask , jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from redis import Redis

from flask_cors import CORS, cross_origin
# ______________________________________________________________________

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'development':
        app.config.from_object('config.ConfigDev')
    else:
        app.config.from_object('config.ConfigPro')
    
    return app 

app = create_app() 

db = SQLAlchemy(app)

redis = Redis()
CORS(app)

# ______________________________________________________________________
from my_app.mod_catalog.database import Product, Category
from my_app.mod_catalog.views import catalog

app.register_blueprint(catalog)

# ______________________________________________________________________

@app.route('/')
def index():
    return '{} {}'.format(app.config['CHECK_ENV'], app.config['SECRET_KEY'])

# _______________________

@app.route('/check_db_conection')
def check_db_conection():
    
    all_products = Product.query.all()

    res = []

    for pro in all_products:
        current_product = {'id': pro.id, 'name': pro.name, 'price': float(pro.price)}
        res.append(current_product)

    print('>>',res)    

    return jsonify(res)


# ______________________________________________________________________


