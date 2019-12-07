#Main file needed to start the app
#Requires setting of environment variables in the ~/.bashrc file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#Set environment variables to connect to the correct mySQL database hosted on a GCP instance
sql_user = getenv('MYSQL_USER')
sql_pass = getenv('MYSQL_PASSWORD')
sql_url = getenv('MYSQL_HOST')
sql_db = getenv('MYSQL_DB')
sql_key = getenv('YOUR_SECRET_KEY')
#Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + sql_user + ':' + sql_pass + '@' + sql_url + '/' + sql_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = sql_key
#Initiates the database 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
