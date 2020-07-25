import os
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.db import db
from app.views.productsBP import productsBP 
from app.views.brandBP import brandBP 
from app.models.productModel import ProductType, Product

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
        #ProductType("Food", "To calm the hunger").save_to_db()
        #ProductType("Drinks", "To refresh yourself").save_to_db()
        #ProductType("Desserts", "At last").save_to_db()
        #Product(1, "Hamburger", 6.5, 10, "A 150Gr grilled meat hamburger. The dish comes with potatoes and salad", 15, "/images/hamburger.jpg").save_to_db()
        #Product(2, "Lemonade", 1.5, 7, "250cc limonade", 15, "/images/lemonade.jpg").save_to_db()
        #Product(3, "icecream", 2, 7, "Vanille ice cream with or baked cake", 14, "/images/icecream.jpg").save_to_db()


    # a simple page that says hello
    @app.route('/')
    def root():
        return redirect(url_for('products.showCatalogue'))

    app.register_blueprint(productsBP)
    app.register_blueprint(brandBP)

    return app
