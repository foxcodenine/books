from my_app import db 

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(6,2), nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price 

    def __repr__(self):
        return '<Product {} {}>'.format(self.id, self.name)