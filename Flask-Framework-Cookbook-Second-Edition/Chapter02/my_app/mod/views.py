from flask import Blueprint,  render_template, request 

hello = Blueprint('hello', __name__, url_prefix='/hello')


# ______________________________________________________________________ 


@hello.route('/')
def hello_world():
    user = request.args.get('user', 'Christopher')
    return render_template('hello.html', user=user)


# http://127.0.0.1:5000/hello/?user=James%20Gauci

# ________________________
