from api.version1.all_orders import app
from flask import request, jsonify

orders_list = [
		{
			"parcelID" : 1,
			"sender_name" : "Jane Doe",
			"sender_email" : "janedoe@test.com",
			"pick_up" : "Nairobi",
			"drop_off" : "Mombasa",
			"recipient_name" : "John Doe",
			"weight" : 4,
			"cost" : 200,
			"status" : "Delivered"
		},
		{
			"parcelID" : 2,
			"sender_name" : "John Doe",
			"sender_email" : "johndoe@test.com",
			"pick_up" : "Kisumu",
			"drop_off" : "Machakos",
			"recipient_name" : "Jane Doe",
			"weight" : 4,
			"cost" : 200,
			"status" : "In transit"
		}
	]   

class SendItOrders():			
	def get_length(self):
		length = len(orders_list)
		return length

	def new_orders(self):
		
		new_order = {
			"parcelID" : orders_list[-1]['parcelID'] + 1,
			"sender_name" : request.json['sender_name'],
			"sender_email" : request.json['sender_email'],
			"pick_up" : request.json['pick_up'],
			"drop_off" : request.json['drop_off'],
			"recipient_name" : request.json['recipient_name'],
			"weight" : request.json['weight'],
			"cost" : 200,
			"status" : "Order requested"
		} 

		orders_list.append(new_order)

		if  orders_list[-1]["sender_name"] == "" or orders_list[-1]["sender_email"] == "" or orders_list[-1]["pick_up"] == "" or orders_list[-1]["drop_off"] == "" or orders_list[-1]["recipient_name"] == "" or orders_list[-1]["weight"] == "":
			orders_list.pop()
			return {"message" : "fields cannot be empty"}

		if orders_list[-1]["weight"] <= 0:
			orders_list.pop()
			return {"message" : "weight cannot be zero "}
			
		return orders_list[-1]

	def all_orders(self):
		if len(orders_list) == 0:
			return {"message" : "No orders in the system"}
		return orders_list