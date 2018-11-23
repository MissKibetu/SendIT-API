from api import app
from flask import request, jsonify
from api.v2.ViewOrders.view_orders import ViewOrders

viewOrderObject = ViewOrders()

""" Fetch all orders. Users can only access their orders. Admin can fetch all orders """

@app.route('/api/v2/fetch_orders', methods=['GET'])
def fetch_my_orders():
    return viewOrderObject.get_my_orders()

@app.route('/api/v2/fetch_orders/<string:parcelID>', methods=['GET'])
def fetch_order_by_id(parcelID):
    return viewOrderObject.get_order_by_id(parcelID)

@app.route('/api/v2/user_orders_by_email', methods=['GET'])
def fetch_user_order_by_email():
    return viewOrderObject.user_order_by_email()

    