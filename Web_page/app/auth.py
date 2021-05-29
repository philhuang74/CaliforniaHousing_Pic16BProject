from flask import Blueprint, current_app, g, render_template, redirect, request, flash, url_for, session
from flask.cli import with_appcontext

from werkzeug.security import check_password_hash, generate_password_hash

import sqlite3
import click

import random
import string

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def get_auth_db():
    if 'db' not in g:
        g.auth_db = sqlite3.connect('users.sqlite')

    return g.auth_db

def close_auth_db(e=None):
    db = g.pop('auth_db', None)

    if db is not None:
        db.close()

# here's how we could initialize our SQL database using Flask
def init_auth_db():
    db = get_auth_db()

    with current_app.open_resource('init.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-auth-db')
@with_appcontext
def init_auth_db_command():
    """Clear the existing data and create new tables."""
    init_auth_db()
    click.echo('Initialized the user database.')


@auth_bp.route('/')
def main():
    return render_template('auth/main.html')

@auth_bp.route('/login/', methods=['POST', 'GET'])
def login():
    if 'user_id' in session:
        flash('Already logged in.')
        return redirect(url_for('auth.main'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_auth_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        print(user)

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[3], password + user[2]):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user[0]
            flash('Successfully logged in.')
            return redirect(url_for('auth.main'))

        flash(error)

    return render_template('auth/login.html')

@auth_bp.route('/register/', methods=['POST', 'GET'])
def register():
    if 'user_id' in session:
        flash('Already logged in.')
        return redirect(url_for('auth.main'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_auth_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
            db.execute(
                'INSERT INTO user (username, salt, password) VALUES (?, ?, ?)',
                (username, salt, generate_password_hash(password + salt))
            )
            db.commit()
            flash('Account created successfully.')
            return redirect(url_for('auth.main'))

        flash(error)

    return render_template('auth/register.html')

@auth_bp.route('/user/', methods=['POST', 'GET'])
def user():
    if 'user_id' not in session:
        flash('Not logged in.')
        return redirect(url_for('auth.main'))
    elif request.method == 'POST':
        session.clear()
        flash('Logged out.')
        return redirect(url_for('auth.main'))
    else:
        db = get_auth_db()
        print(session['user_id'])
        user = \
          db.execute('SELECT * FROM user WHERE id = ?', str(session['user_id'])).fetchone()
        return render_template('auth/user.html', username=user[1])
