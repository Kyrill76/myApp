from myApp import app, db
from myApp.Guid import GUID
import uuid

import datetime

# Authentification
from passlib.apps import custom_app_context as pwd_context # or md5_crypt as pwd_context
#https://pythonhosted.org/passlib/lib/passlib.hash.html
#Token auth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


class User(db.Model):
    __tablename__ = 'User'

    Id = db.Column(GUID(), primary_key=True)
    Login = db.Column(db.String(140), index=True)
    password_hash = db.Column(db.String(200))
    FirstName = db.Column(db.String(140))
    LastName = db.Column(db.String(140))

    CreationDate = db.Column(db.DateTime)
    LastModificationDate = db.Column(db.DateTime)


    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=3600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        IdString = "{0}".format(self.Id)
        return s.dumps({'Id': IdString})

    def __unicode__(self):
        return self.Login

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['Id'])
        return user

    def __init__(self, *args, **kwargs):

        self.Login = kwargs.get('Login')
        self.FirstName = kwargs.get('FirstName')
        self.LastName = kwargs.get('LastName')

    def dict_format(self):
        return dict(
            Id=self.Id,
            Login=self.Login,
            FirstName=self.FirstName,
            LastName=self.LastName,
            CreationDate=self.CreationDate,
            LastModificationDate=self.LastModificationDate)
