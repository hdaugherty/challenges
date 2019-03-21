from flask import render_template, url_for, flash, redirect
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post
from flask_login import login_user, current_user
from datetime import datetime, time

# Logic for the timers


# Temporary data to use
posts = [
    {
        'author': 'Holden Daugherty',
        'title': "Holden's Goals",
        'content': 'Study Goals',
        'date_posted': 'March 16, 2019'
    },
    {
        'author': 'Joe Bob',
        'title': "Joe's Goals",
        'content': 'Study Goals',
        'date_posted': 'March 10, 2019'
    }
]


# Route to the home page
# This route also use multiple decorators to let / and
# /home represent the homepage.
@app.route('/')
@app.route('/home')
def home():
    # Uses the render_template method in flask to render the home.html page
    # and assign posts data to the posts attribute
    return render_template('home.html', posts=posts)


# Route to the about page, which explain the purpose of the site.
@app.route('/about')
def about():
    return render_template('about.html', title='About')


# Route to the register page, for users to register to the site
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Since this page will accept user data it is a form and we must create the
    # form first.
    form = RegistrationForm()

    # Redirect the user to Home when they click login/register while logged in
    if current_user.is_authenticated:
        flash("You're already logged in!")
        return redirect(url_for('home'))

    if form.validate_on_submit():
        # Hashing the password that user entered
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Create an instance of a user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # and adding them to the database
        db.session.add(user)
        db.session.commit()
        # the flash method will flash a message to the user.
        flash(f'Your account has been created {form.username.data}! You are now able to log in.', 'success')

        # Use the redirect method buitin to flask and the url_for method to redirect
        # the user back to the 'home' page, which is the method used in the home route.
        return redirect(url_for('login'))

    # This render_template also assigns a title to change the tab title
    return render_template('register.html', title='Register', form=form)


# Route to the login page, for already registered users
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Again this is a form because it accepts data
    form = LoginForm()

    # Redirect the user to Home when they click login/register while logged in
    if current_user.is_authenticated:
        flash("You're already logged in!")
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, check email & password.', 'danger')
    return render_template('login.html', title='Login', form=form)
