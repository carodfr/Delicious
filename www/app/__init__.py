import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.db import db
from app.views.productsBP import productsBP 

def create_app():

    # create and configure the app
    app = Flask(__name__)

    # load dotenv in the base root
    APP_ROOT = os.path.join(os.path.dirname(__file__), '.')   # refers to application_top
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
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
