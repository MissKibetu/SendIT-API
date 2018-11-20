from flask import Flask
app = Flask(__name__)

import api.db_config
import api.v1.orders.views   
import api.v2.signup_signin.views
     