from flask import Blueprint, request, session, url_for, render_template, flash
from app.models.userModel import User 

userBP = Blueprint('user', __name__, url_prefix='/user')

@userBP.route('/register')
def register():
    return render_template('register.html')

@userBP.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['inputUser']
        password = request.form['inputPassword']
        loginUser=User.check_login(username, password)
        if loginUser:
            session['username'] = username
            return redirect(url_for('/'))
        else:
            flash('Please review your login information')
    return render_template('login.html')
