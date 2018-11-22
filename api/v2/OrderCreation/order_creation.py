from api import app
from api.db_config import con, cur
from flask import request, jsonify
from api.v2.validations.models import Validations

validationObject = Validations()

class OrderCreation():

	def order_request(self, email):
		email_check = validationObject.email_check(email)
		pick_up = request.json['pick_up']
		drop_off = request.json['drop_off']
		recipient_name = request.json['recipient_name']
		weight = request.json['weight']

		if any(user_input == "" for user_input in (pick_up, drop_off, recipient_name,weight)):
			return "fields cannot be empty"

		if weight <= 0:
			return "weight cannot be zero"

		if email_check:
			role_check = validationObject.role_check(email)
			role = "admin"
		
			if role_check != role:
				result = cur.execute ("SELECT name, email FROM users WHERE email = (%s)", ([email]))
				result = cur.fetchall()

				if result:
					output = {"cost" : 200,
						"status" : "Order requested",
						"pick_up": pick_up,
						"drop_off": drop_off,
						"recipient_name" : recipient_name,
						"weight" : weight,
						"current_location": request.json['pick_up']
						}

					for row in result:
						output.update({'name': row[0], 'email': row[1] })

					cur.execute("INSERT INTO orders(sender_name, sender_email, pick_up, drop_off, recipient_name,weight, cost, status, current_location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (output['name'], output['email'], output['pick_up'], output['drop_off'], output['recipient_name'], output['weight'], output['cost'], output['status'], output['current_location']))
					con.commit()
					return "Order created"
			
			return "Orders cannot be created on admin account"
			
		return "email not registered"
