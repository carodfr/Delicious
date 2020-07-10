from flask import (Blueprint, render_template)


productsBP = Blueprint('products', __name__, url_prefix='/products')

@productsBP.route('/buy', methods=('GET', 'POST'))
def listProducts():
    return render_template('catalog.html')
