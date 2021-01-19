from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)
params = urllib.parse.quote_plus('Driver={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-JDTJBITQ\MSSQLSERVER01;DATABASE=ESL_SORTER;UID=paulo;PWD=30051998;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
db = SQLAlchemy(app)