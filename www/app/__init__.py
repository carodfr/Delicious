import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.db import db
from app.views.productsBP import productsBP 

def create_app():

    # create and configure the app
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:TGdxctSoUtqbMoZaDLne@storedb.c8k7qd9rz8qw.eu-central-1.rds.amazonaws.com/storedb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.secret_key = os.urandom(64)

    db.init_app(app)


    @app.before_first_request
    def create_tables():
        db.create_all()

    # a simple page that says hello
    @app.route('/test')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(productsBP)

    return app
