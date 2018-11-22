from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

from api.db_config import DbConfig
db = DbConfig()
db.create_tables()


app.config['JWT_SECRET_KEY'] = 'secretkey'
jwt = JWTManager(app)


import api.v1.orders.views   
import api.v2.User.views
import api.v2.OrderCreation.views

