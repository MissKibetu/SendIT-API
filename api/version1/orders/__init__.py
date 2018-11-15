from flask import Flask
app = Flask(__name__)

import api.version1.orders.views   
     