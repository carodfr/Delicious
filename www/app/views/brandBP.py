from flask import (Blueprint, render_template)
#from app.models.caseModel import Case

brandBP = Blueprint('brand', __name__, url_prefix='/brand')

@brandBP.route('/about')
def about():
    #products=Product.query.all()
    return render_template('about.html')

@brandBP.route('/support')
def support():
    return render_template('support.html')
