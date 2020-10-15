from flask_wtf import FlaskForm 
from wtforms import StringField, DecimalField, SelectField 


class ProductForm(FlaskForm):
    name = StringField('Name')
    price = DecimalField('Price')
    category = SelectField('Category', coerce=int)
    
    # coerce=int  - his means that the incoming data from the HTML form
    # will be coerced to an integer value prior to validating or any
    # other processing