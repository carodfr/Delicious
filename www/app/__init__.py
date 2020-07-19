import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.db import db
from app.views.productsBP import productsBP 
from app.views.brandBP import brandBP 

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
    @app.route('/')
    def root():
        return redirect(url_for('productsBP.showCatalog'))

    app.register_blueprint(productsBP)
    app.register_blueprint(brandBP)

    return app
