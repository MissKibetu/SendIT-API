from api.v1.orders import app
from flask import jsonify
from api.v1.orders.models import SendItOrders

ordersObject = SendItOrders()

"""This route creates and adds new order to currents order list"""

@app.route('/api/v1/create_order', methods=['POST'])
def create_new_order():
    orders = ordersObject.new_orders()
    return jsonify({"orders: " :orders}), 201

"""This route fetches all orders in the system"""

@app.route('/api/v1/all_orders', methods=['GET'])
def get_all_orders():
    orders = ordersObject.all_orders()
    return jsonify({"orders: " :orders}), 200

"""This route fetches the order with the id specified in the route"""

@app.route('/api/v1/all_orders/<int:parcelID>', methods=['GET'])
def get_order_by_ID(parcelID):
    orders = ordersObject.order_by_ID(parcelID)
    return jsonify({"orders: " :orders}), 200

"""This route fetches the orders from the email specified in the route"""

@app.route('/api/v1/all_orders/<string:sender_email>', methods=['GET'])
def get_all_orders_by_sender_email(sender_email):
    orders = ordersObject.all_orders_by_sender_email(sender_email)
    return jsonify({"orders: " :orders}), 200

"""This route cancels the order with the id specified in the route"""

@app.route('/api/v1/cancel/<int:parcelID>', methods=['PUT'])
def cancel_order_by_parcelID(parcelID):
    orders = ordersObject.cancel_order(parcelID)
    #order =ordersObject
    return jsonify({"message" : orders}), 200
    