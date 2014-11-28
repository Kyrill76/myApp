#postgresql:
db_conn = 'postgresql+psycopg2://user:password@localhost/database'

SQLALCHEMY_DATABASE_URI = db_conn

#Token auth
SECRET_KEY = ‘this is a secret key’

SQLALCHEMY_ECHO = True

DEBUG = True
