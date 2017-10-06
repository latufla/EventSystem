from functools import wraps

from flask import session, redirect, url_for


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


def is_not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' not in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


def is_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session["admin"]:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login')) # logout

    return wrap
