from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import User, Post


# Create the instance of an flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8ac04cff43b2ea6dcfbe2006aa40455a82b7512a'

# Set site.db a relative path from the current file system as the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Instantiate the database
db = SQLAlchemy(app)



# Temporary data to use 
posts = [
	{
		'author': 'Holden Daugherty',
		'title': 'Holden\'s Goals',
		'content': 'Study Goals',
		'date_posted': 'March 16, 2019'
	},
	{
		'author': 'Joe Bob',
		'title': 'Joe\'s Goals',
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
	if form.validate_on_submit():
		# the flash method builtin to flask will flash a message to the user.
		flash(f'Account created for {form.username.data}!', 'success')

		# Use the redirect method buitin to flask and the url_for method to redirect
		# the user back to the 'home' page, which is the method used in the home route.
		return redirect(url_for('home'))

	# This render_template also assigns a title to change the tab title 
	return render_template('register.html', title='Register', form=form)


# Route to the login page, for already registered users
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'Successful login!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login unsuccessful, check username & password.', 'danger')
	return render_template('login.html', title='Login', form=form)


# Main method that lets us use python 'app.name' in terminal to run the
# the application in debug mode.
if __name__ == '__main__':
    app.run(debug=True)
