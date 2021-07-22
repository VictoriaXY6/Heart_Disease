from flask import Blueprint, render_template, request, redirect, url_for, flash, Markup
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from ..helper import get_user_email, add_to_database
from ..models import Writer

# create a Blueprint object called auth.
auth = Blueprint('auth', __name__, 
                template_folder='templates', 
                static_folder='static',
                static_url_path='')
# login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        # find the user according to the email
        user = get_user_email(email)
        
        # print error message when user not found or password not match
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login detail and try again.', 'danger')
        else:
            # if the above check passes, then we know the user has the right credentials
            login_user(user, remember=remember)
            return redirect(url_for('main.profile'))
    
    return render_template('auth/login.html', page_title='Login In')

# signup page
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #obtain email with all lower case character, name and password from the signup page
        email = request.form.get('email').lower()
        name = request.form.get('name')
        password = request.form.get('password')

        # check if the user already exist in the Writer table
        user = get_user_email(email)

        if user:
            # send message to login in pages when user already exist
            flash(Markup('Email address already exists. Go to <a href="/login">login page</a>'), 'warning')
        else:
            # add the new user to the table
            new_user = Writer(email, password, name)
            add_to_database(new_user)
            #successful create account
            flash('Successful create account', 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', page_title='Sign Up')
    

# logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
