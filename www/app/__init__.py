from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from productsBP import productsBP 

db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__)
    #db.init_app(app)

    app.register_blueprint(productsBP)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
