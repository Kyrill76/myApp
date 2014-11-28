from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='files')
app.config.from_object('myApp.config')

db = SQLAlchemy(app)
auth = HTTPBasicAuth()


import UserModel, UserRoutes, AdminView
