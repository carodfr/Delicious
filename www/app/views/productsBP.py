from flask import (Blueprint, render_template)
from app.models.productModel import Product

productsBP = Blueprint('products', __name__, url_prefix='/products')

@productsBP.route('/catalogue')
def showCatalogue():
    products=Product.query.all()
    return render_template('catalogue.html', products=products)

@productsBP.route('/checkout')
def checkout():
    return render_template('catalog.html')
