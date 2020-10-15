from my_app import db 

# ____________________________

# The following relationtionship is many-to-one, 
# It is slightly different from one-to-many relastionship

# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(6, 2), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products', lazy='dynamic'))

    def __init__(self, name, price, category):
        self.name = name
        self.price = price 
        self.category = category

    def __repr__(self):
        return '<Product {} {}>'.format(self.id, self.name)

# ____________________________

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Product {} {}>'.format(self.id, self.name)

# ____________________________