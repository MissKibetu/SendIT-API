from api import app
from flask import request, jsonify
from api.v2.UpdateOrders.update_order import UpdateOrders

updateObject = UpdateOrders()

@app.route('/api/v2/change_destination/<string:email>', methods=['PUT'])
def change_parcel_destination(email):

    return jsonify({"message": updateObject.change_destination(email)}), 200

@app.route('/api/v2/change_current_location/<string:email>', methods=['PUT'])
def change_current_destination(email):
    
    return jsonify({"message": updateObject.update_current_location(email)}), 200