from flask import Blueprint, render_template, request, flash
from app.models.productModel import ProductType
from app.security import requires_permission

productsBP = Blueprint('products', __name__, url_prefix='/products')

@productsBP.route('/catalogue')
def showCatalogue():
    productTypes=ProductType.query.all()
    return render_template('catalogue.html', productTypes=productTypes)

@productsBP.route('/checkout', methods=['POST'])
@requires_permission('Administrator', 'Client')
def checkout():
    cart = request.form['cart']
    flash(cart)
    return render_template('checkout.html')
