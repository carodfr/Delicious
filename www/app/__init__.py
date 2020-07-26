import os
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.db import db
from app.views.productsBP import productsBP 
from app.views.brandBP import brandBP 
from app.views.userBP import userBP 

from app.models.productModel import ProductType, Product
from app.models.userModel import Role, User
#from app.models.orderModel import OrderStatus

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

    #initialization of the database and the initial data
    @app.before_first_request
    def create_database():
        db.create_all()
#        ProductType.init_data()
#        Product.init_data()
#        Role.init_data()
#        User.init_data()
#        OrderStatus.init_data()

    # redirection to the catalogue page
    @app.route('/')
    def root():
        return redirect(url_for('products.showCatalogue'))

    app.register_blueprint(productsBP)
    app.register_blueprint(brandBP)
    app.register_blueprint(userBP)

    return app
