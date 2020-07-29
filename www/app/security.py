import functools
from flask import session, redirect, url_for
from app.models.userModel import User

def requires_permission(*permissions):
    def decorator(f):
        @functools.wraps(f)
        def secure_function(*args, **kwargs):
            if('username' in session.keys() and session['username'] and User.find_by_username(session['username']).role.name in permissions):
                return f(*args, **kwargs)
            return redirect(url_for('user.login'))
        return secure_function
    return decorator


