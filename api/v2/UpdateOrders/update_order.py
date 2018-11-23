from api import app
from api.db_config import con, cur
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from api.v2.validations.models import Validations

validationObject = Validations()

class UpdateOrders():

	""" User can update destination """
	@jwt_required
	def change_destination(self):
		email = get_jwt_identity()
		drop_off = request.json['drop_off']
		parcelID = request.json['parcelID']

		if any(user_input == "" for user_input in (drop_off, parcelID)):
			return {"message" : "fields cannot be empty"}

		email_check = validationObject.email_check(email)
		
		if email_check:
			cur.execute ("SELECT * FROM orders WHERE parcelID = (%s)", (parcelID))
			order_table = cur.fetchall()

			if order_table:
				output = []
				for row in order_table:
					output.append({'parcelID': row[0], 'sender_name': row[1], 'sender_email': row[2], 'pick_up': row[3], 'drop_off': row[4], 'recipient_name': row[5], 'weight': row[6], 'cost': row[7],'status': row[8], 'current_location': row[9]})
					if email != row[2]:
						return "Your credentials do not match that order"
					if drop_off == row[4]:
						return "Change not made. New drop off location matches current drop off location."

					cur.execute("UPDATE orders SET drop_off = (%s) WHERE parcelID = (%s)", (drop_off, parcelID))
					con.commit()
					return "order updated"
			return "No order with that ID"
							
		return "unregistered email"

	
	""" User can update destination """
	@jwt_required
	def update_current_location(self):
		admin_email = get_jwt_identity()
		parcelID = request.json['parcelID']
		current_location = request.json['current_location']
		transit_status = "In transit"
		delivered_status = "Delivered"

		if any(user_input == "" for user_input in (current_location, parcelID)):
			return {"message" : "fields cannot be empty"}

		email_check = validationObject.email_check(admin_email)
		
		if email_check:
			role_check = validationObject.role_check(admin_email)

			if role_check == "admin":	
				cur.execute ("SELECT * FROM orders WHERE parcelID = (%s)", (parcelID))
				order_table = cur.fetchall()

				if order_table:
					output = []
					for row in order_table:
						output.append({'parcelID': row[0], 'sender_name': row[1], 'sender_email': row[2], 'pick_up': row[3], 'drop_off': row[4], 'recipient_name': row[5], 'weight': row[6], 'cost': row[7],'status': row[8], 'current_location': row[9]})
						if current_location == row[4]:
							cur.execute("UPDATE orders SET current_location = (%s), status = (%s) WHERE parcelID = (%s)", (current_location, delivered_status, parcelID))
							con.commit()
							return "order updated"
						cur.execute("UPDATE orders SET current_location = (%s), status = (%s) WHERE parcelID = (%s)", (current_location, transit_status, parcelID))
						con.commit()
						return "order updated"

				return "No order with that ID"

			return "You do not have admin rights"

		return "unregistered email"

