from myApp import app, db, auth
from UserModel import User
from flask import abort, request, jsonify, g, url_for
from datetime import datetime


#___AUTHENTIFICATION CHECK_____________________________
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(Login=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

#___USER REGISTRATION__________________________________
@app.route('/api/registerUser', methods=['POST'])
def new_user():
    login = request.json.get('Login')
    password = request.json.get('password')
    if login is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(Login=login).first() is not None:
        abort(400) # existing user
    user = User(Login=login)
    user.hash_password(password)
    user.FirstName = request.json.get('FirstName')
    user.LastName = request.json.get('LastName')

    user.CreationDate = datetime.utcnow()
    db.session.add(user)
    db.session.commit()

    user_dict = user.dict_format()
    formatted_result = dict(User=user_dict)
    
    return jsonify(result=formatted_result)


@app.route('/api/users/')
def get_users():
    if request.method == 'GET':

        results = User.query.all()

        json_results = []
        for result in results:
            d = {'Login': result.Login}
            json_results.append(d)

        return jsonify(items=json_results)


@app.route('/api/login')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(3600)
    user_dict = g.user.dict_format()

    session_details_dict = dict(
        Login=g.user.Login,
        token=token.decode('ascii'),
        duration=3600
    )

    return 'OK'


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.Login})
