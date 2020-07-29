from flask import Blueprint, request, redirect, session, url_for, render_template, flash
from app.models.userModel import User 

userBP = Blueprint('user', __name__, url_prefix='/user')

@userBP.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username=request.form['inputUsername']
        password=request.form['inputPassword']
        firstname=request.form['inputFirstname']
        lastname=request.form['inputLastname']
        address=request.form['inputAddress']

        user_exist=User.find_by_username(username)
        if user_exist:
            flash('The username already exist')
        else:
            User.create_client(username, password, firstname, lastname, address).save_to_db()
            session['username'] = username
            return redirect('/')

    return render_template('register.html')

@userBP.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['inputUsername']
        password = request.form['inputPassword']
        login_user=User.check_login(username, password)
        if login_user:
            session['username'] = username
            return redirect('/')
        else:
            flash('Incorrect login information')
    return render_template('login.html')

@userBP.route('/logout')
def logout():
    session['username']=None
    return redirect('/')
