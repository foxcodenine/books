from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager 

from redis import Redis
# ______________________________________________________________________

# db = SQLAlchemy()


# ____________________________

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'development':
        app.config.from_object('config.ConfigDev')
    else:
        app.config.from_object('config.ConfigPro')

   

    return app 

app = create_app()

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

redis = Redis() 


# ______________________________________________________________________

class TestTable(db.Model):
    __tablename__ = 'test_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)


# ______________________________________________________________________


@app.route('/')
def index():
    return '<h4>{}</h4>'.format(app.config['CHECK_ENV'])



# ____________________________

@app.route('/db')
def my_db():

    db.create_all()
    db.session.commit()

    message = 'This is the database check route!'

    return '<h4>{}</h4>'.format(message)

# ______________________________________________________________________


from my_app.mod_catalog.views import catalog

app.register_blueprint(catalog)


# ______________________________________________________________________

'''
Request Data

>> python

import request

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'iPhone 5S', 'price': '549.0', 'category': 'phone'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'Seiko 143', 'price': '1200', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'Garmin 426', 'price': '310.0', 'category': 'electronics'})

requests.post('http://127.0.0.1:5000/catalog/product-create',
data={'name': 'Black Bay 58', 'price': '6300', 'category': 'watch'})

requests.post('http://127.0.0.1:5000/catalog/category-create',
data={'name': 'jewellery'})

requests.post('http://127.0.0.1:5000/catalog/category-create',
data={'name': 'gadgets'})

'''
