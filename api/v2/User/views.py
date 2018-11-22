from api import app
from flask import request,jsonify
from api.v2.User.user import User

usersObject = User()

@app.route('/api/v2/signup', methods=['POST'])
def register_user():
    """ User signup """
    return jsonify({"message": usersObject.user_signup()}), 200
    

@app.route('/api/v2/signin', methods=['POST'])
def login():
    """ User signin """
    return usersObject.user_login(), 200

@app.route('/api/v2/change_role_to_admin/<string:email>', methods=['PUT'])
def change_role(email):
    """ Change user role to Admin """ 
    return jsonify({"message": usersObject.admin_account(email)}), 200

