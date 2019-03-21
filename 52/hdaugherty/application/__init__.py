from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create the instance of an flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8ac04cff43b2ea6dcfbe2006aa40455a82b7512a'

# Set site.db a relative path from the current file system as the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Instantiate the database
db = SQLAlchemy(app)

# Create an instance of bcrypt for password hashing
bcrypt = Bcrypt(app)

# Create an instance of LoginManager for the login process
login_manager = LoginManager(app)

from application import routes
