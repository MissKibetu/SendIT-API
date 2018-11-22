from api import app
from flask import request, jsonify
from api.v2.OrderCreation.order_creation import OrderCreation

orderObject = OrderCreation()

""" order by email. Simulate order placement after login """

@app.route('/api/v2/order_request/<string:email>', methods=['POST'])
def order_by_email(email):
    return jsonify({"message": orderObject.order_request(email)}), 201