import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)

    from . import app_mongoalchemy
    app.register_blueprint(app_mongoalchemy.bp)
    app.add_url_rule('/', endpoint='index')

    return app
