from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://'+getenv('MYSQL_USER')+':'+getenv('MYSQL_PASSWORD')+'@'+getenv('MYSQL_HOST')+'/'+getenv('MYSQL_DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = (getenv('YOUR_SECRET_KEY'))
db = SQLAlchemy(app)

from application import routes
