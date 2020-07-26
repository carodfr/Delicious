from flask import Blueprint, request, session, url_for, render_template
from app.models.userModel import User 

userBP = Blueprint('user', __name__, url_prefix='/user')

@userBP.route('/register')
def register():
    return render_template('register.html')

@userBP.route('/login')
def login():
    return render_template('login.html')
