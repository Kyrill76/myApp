from myApp import app
from UserModel import User


#flask-admin sqla
from flask.ext.admin.contrib import sqla

from flask import Flask
from flask.ext.admin import Admin

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Homepage</a>'


class AdminView(sqla.ModelView):
    can_delete = True
    can_edit = True
    can_create = True
