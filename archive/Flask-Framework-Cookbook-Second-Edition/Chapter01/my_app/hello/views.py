
from flask import Blueprint
from my_app.hello.models import MESSAGES

# ______________________________________________________________________ 

hello = Blueprint('hello', __name__, url_prefix='/hello')

# ________________________

@hello.route('/')
@hello.route('/hello/')
def hello_world():
    return MESSAGES['default']
# ________________________

@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!"%key

# ________________________

@hello.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    
    MESSAGES[key] = message
    return "{} Added/Updated".format(key)
    
# ________________________