from flask_wtf import FlaskForm 
from wtforms import StringField, DecimalField, SelectField 


class ProductForm(FlaskForm):
    name = StringField('Name')
    price = DecimalField('Price')
    category = SelectField('Category', coerce=int) 
    # <- we specified the choices at the view (/product-create').
    
    # coerce=int  - this means that the incoming data from the HTML form
    # will be coerced to an integer value prior to validating or any
    # other processing.