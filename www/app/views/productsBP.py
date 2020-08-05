from flask import Blueprint, render_template, request, flash, session, redirect
import json

from app.models.productModel import ProductType, Product
from app.models.userModel import User
from app.models.orderModel import Order
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

    dict_cart=json.loads(request.form['cart'])
    registerReceipt=lambda product, quantity :{"name":product.name, "description":f"{quantity} unit(s) - {product.price} EUR per unit", "value":product.price*quantity}
    receipt = [registerReceipt(Product.find_by_id(key), dict_cart[key]) for key in dict_cart]
    total=sum([register['value'] for register in receipt])

    return render_template('checkout.html', user=user, receipt=receipt, total=total)


@productsBP.route('/orders', methods=['GET', 'POST'])
@requires_permission('Administrator', 'Client')
def complete_transaction():
    current_user=User.find_by_username(session['username'])
    if request.method == 'POST':
        deliveryAddress=request.form['inputDeliveryAddress']
        first_name=request.form['inputFirstName']
        last_name=request.form['inputLastName']
        billing_address=request.form['inputBillingAddress']
        dict_cart=json.loads(request.form['cart'])
        current_order=Order(first_name, last_name, billing_address, current_user.id)
        current_order.save_to_db()
        for product_id in dict_cart:
            current_order.add_product(product_id, dict_cart[product_id])
    if current_user.role.name == 'Administrator':
        return render_template('orders.html', orders=Order.get_all(), allow_update=True)
    else:
        return render_template('orders.html', orders=Order.find_by_user_id(current_user.id), allow_update=False)


@productsBP.route('/orders/<int:order_id>')
@requires_permission('Administrator')
def promote_order(order_id):
    Order.find_by_id(order_id).promote_status()
    return redirect('/products/orders')

