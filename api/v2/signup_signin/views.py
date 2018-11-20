from api import app
from flask import request,jsonify
from api.v2.signup_signin.models import User

usersObject = User()

""" User signup """

@app.route('/api/v2/signup', methods=['POST'])
def register_user():
    new_user = usersObject.user_signup()
    return new_user

""" User signin """

@app.route('/api/v2/signin', methods=['POST'])
def login():
    user = usersObject.user_login()
    return user