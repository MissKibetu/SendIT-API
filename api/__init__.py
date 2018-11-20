from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

import api.db_config

app.config['JWT_SECRET_KEY'] = 'secretkey'
jwt = JWTManager(app)

import api.db_config
import api.v1.orders.views   
import api.v2.signup_signin.views
     