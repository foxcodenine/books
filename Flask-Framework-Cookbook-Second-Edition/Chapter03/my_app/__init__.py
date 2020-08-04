from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# ______________________________________________________________________

db = SQLAlchemy()


# ____________________________

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'development':
        app.config.from_object('config.ConfigDev')
    else:
        app.config.from_object('config.ConfigPro')

    db.init_app(app)

    return app 

app = create_app()


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

