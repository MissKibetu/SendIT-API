from api import app
from flask import request, jsonify
from api.v2.UpdateOrders.update_order import UpdateOrders

updateObject = UpdateOrders()

@app.route('/api/v2/change_destination', methods=['PUT'])
def change_parcel_destination():

    return jsonify({"message": updateObject.change_destination()}), 200

@app.route('/api/v2/change_current_location', methods=['PUT'])
def change_current_destination():
    
    return jsonify({"message": updateObject.update_current_location()}), 200