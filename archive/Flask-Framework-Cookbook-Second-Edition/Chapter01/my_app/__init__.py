from flask import Flask
from my_app.hello.views import hello

app = Flask(__name__)

app.register_blueprint(hello)

# ______________________________________________________________________


if app.config['ENV'] == 'development':
    app.config.from_object('config.ConfigDev')
else :
    app.config.from_object('config.ConfigPro')


# ______________________________________________________________________

@app.route('/')
@app.route('/index/')
def index():
    return f'index {app.config["CHECK_ENV"]}'

# ______________________________________________________________________

import my_app.hello.views