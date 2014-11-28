from myApp import app, db
from flask.ext import admin

from myApp.AdminView import AdminView, User

# Create admin
admin = admin.Admin(app, 'Administration')

# Add views
admin.add_view(AdminView(User, db.session))


if __name__ == '__main__':

    #SSL
    from werkzeug.serving import make_ssl_devcert, run_simple

    from OpenSSL import SSL
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.use_privatekey_file('./ssl/myApp.key')
    ctx.use_certificate_file('./ssl/myApp.crt')

    run_simple('vpsxxxxx.ovh.net', 5001, app, ssl_context=ctx, use_debugger=False, threaded=True)
