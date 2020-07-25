from flask import (Blueprint, render_template)
from app.models.productModel import ProductType

productsBP = Blueprint('products', __name__, url_prefix='/products')

@productsBP.route('/catalogue')
def showCatalogue():
    productTypes=ProductType.query.all()
    return render_template('catalogue.html', productTypes=productTypes)

@productsBP.route('/checkout')
def checkout():
    return render_template('checkout.html')
