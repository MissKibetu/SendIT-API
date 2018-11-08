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