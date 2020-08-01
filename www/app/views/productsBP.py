from flask import Blueprint, render_template, request, flash, session
import json

from app.models.productModel import ProductType, Product
from app.models.userModel import User
from app.security import requires_permission

productsBP = Blueprint('products', __name__, url_prefix='/products')

@productsBP.route('/catalogue')
def showCatalogue():
    productTypes=ProductType.query.all()
    return render_template('catalogue.html', productTypes=productTypes)

@productsBP.route('/checkout', methods=['POST'])
@requires_permission('Administrator', 'Client')
def checkout():

    user=User.find_by_username(session['username'])

    dictCart=json.loads(request.form['cart'])
    registerReceipt=lambda product, quantity :{"name":product.name, "description":f"{quantity} unit(s) - {product.price} EUR per unit", "value":product.price*quantity}
    receipt = [registerReceipt(Product.find_by_id(key), dictCart[key]) for key in dictCart]
    total=sum([register['value'] for register in receipt])

    return render_template('checkout.html', user=user, receipt=receipt, total=total)


@productsBP.route('/orders', methods=['GET', 'POST'])
@requires_permission('Administrator', 'Client')
def complete_transaction():
    pass


