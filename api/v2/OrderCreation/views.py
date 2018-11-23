from api import app
from flask import request, jsonify
from api.v2.OrderCreation.order_creation import OrderCreation
from flask_jwt_extended import get_jwt_identity, jwt_required

orderObject = OrderCreation()

""" order by email. Simulate order placement after login """

@app.route('/api/v2/order_request', methods=['POST'])
def order_by_email():
    return jsonify({"message": orderObject.order_request()}), 201
    