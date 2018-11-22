from api import app
from flask import request, jsonify
from api.v2.ViewOrders.view_orders import ViewOrders

viewOrderObject = ViewOrders()

""" Fetch all orders. Users can only access their orders. Admin can fetch all orders """

@app.route('/api/v2/fetch_orders/<string:email>', methods=['GET'])
def fetch_my_orders(email):
    return viewOrderObject.get_my_orders(email)

@app.route('/api/v2/fetch_orders/<string:email>/<string:parcelID>', methods=['GET'])
def fetch_order_by_id(email, parcelID):
    return viewOrderObject.get_order_by_id(email, parcelID)

@app.route('/api/v2/user_orders_by_email/<string:admin_email>/<string:user_email>', methods=['GET'])
def fetch_user_order_by_email(admin_email, user_email):
    return viewOrderObject.user_order_by_email(admin_email, user_email)