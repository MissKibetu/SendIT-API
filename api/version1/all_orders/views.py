from api.version1.all_orders import app
from flask import jsonify
from api.version1.all_orders.models import SendItOrders

ordersObject = SendItOrders()
length = ordersObject.get_length()

@app.route('/api/v1/home', methods=['GET'])
def home():
    welcome_message1 = "Hello! Welcome to SendIT - see orders here. "
    return welcome_message1

@app.route('/api/v1/create_order', methods=['POST'])
def create_new_order():
    orders = ordersObject.new_orders()
    return jsonify({"orders: " :orders}), 201

@app.route('/api/v1/all_orders', methods=['GET'])
def get_all_orders():
    orders = ordersObject.all_orders()
    return jsonify({"orders: " :orders}), 200