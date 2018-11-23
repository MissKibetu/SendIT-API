from api import app
from api.db_config import con, cur
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from api.v2.validations.models import Validations

validationObject = Validations()

class ViewOrders():
	
	""" Fetch all orders """
	@jwt_required
	def get_my_orders(self):
		email = get_jwt_identity()
		email_check = validationObject.email_check(email)

		if email_check:
			role_check = validationObject.role_check(email)
			role = "admin"

			""" Users can only access their orders """

			if role_check != role:
				order_table = cur.execute ("SELECT * FROM orders WHERE sender_email = '{}';".format(email))
				order_table = cur.fetchall()	

				if order_table:
					
					output = []

					for row in order_table:
						output.append({'parcelID': row[0], 'sender_name': row[1], 'sender_email': row[2], 'pick_up': row[3], 'drop_off': row[4], 'recipient_name': row[5], 'weight': row[6], 'cost': row[7],'status': row[8], 'current_location': row[9]})

					return (jsonify({'Your orders': output}))
				
				return jsonify({"message": "list is empty"})

			""" Admin can fetch all orders """
			
			if role_check == role:
				admin_order_table = cur.execute ("SELECT * FROM orders")
				admin_order_table = cur.fetchall()	

				if admin_order_table:
					
					output = []

					for row in admin_order_table:
						output.append({'parcelID': row[0], 'sender_name': row[1], 'sender_email': row[2], 'pick_up': row[3], 'drop_off': row[4], 'recipient_name': row[5], 'weight': row[6], 'cost': row[7],'status': row[8], 'current_location': row[9]})

					return (jsonify({'orders in the system': output}))
				
				return jsonify({"message": "list is empty"})			
		
		return jsonify({"message": "unregistered email"})

	""" Fetch order by ID """

	@jwt_required
	def get_order_by_id(self, parcelID):
		email = get_jwt_identity()
		email_check = validationObject.email_check(email)
		
		if email_check:
			cur.execute ("SELECT * FROM orders WHERE parcelID = (%s)", ([parcelID]))
			order_table = cur.fetchall()
			
			if order_table:
				output = []

				for row in order_table:
					output.append({'parcelID': row[0], 'sender_name': row[1], 'sender_email': row[2], 'pick_up': row[3], 'drop_off': row[4], 'recipient_name': row[5], 'weight': row[6], 'cost': row[7],'status': row[8], 'current_location': row[9]})
					role_check = validationObject.role_check(email)
					if (role_check == "user") and (email != row[2]):

						return jsonify({"message": "Your credentials do not match that order"})

					return (jsonify({'Order Details': output}))
			
			return jsonify({"message": "No order with that ID"})

		return jsonify({"message": "unregistered email"})	

	""" Fetch order by email """
	
	@jwt_required
	def user_order_by_email(self):
		admin_email = get_jwt_identity()
		user_email = request.json['user_email']
		admin_email_check = validationObject.email_check(admin_email)
			
		if admin_email_check:
			admin_role_check = validationObject.role_check(admin_email)

			if admin_role_check == "admin":
				user_email_check = validationObject.email_check(user_email)

				if user_email_check:					
					cur.execute ("SELECT * FROM orders WHERE sender_email = (%s)", ([user_email]))
					order_table = cur.fetchall()

					if order_table:
						output = []

						for row in order_table:
							output.append({'parcelID': row[0], 'sender_name': row[1], 'sender_email': row[2], 'pick_up': row[3], 'drop_off': row[4], 'recipient_name': row[5], 'weight': row[6], 'cost': row[7],'status': row[8], 'current_location': row[9]})
						return (jsonify({'Order Details': output}))

					return jsonify({"message": "No orders made by the customer"})

				return jsonify({"message": "The user email provided is unregistred"})

			return jsonify({"message": "You do not have admin rights!"})		
					
		return jsonify({"message": "You are not a registered user. Please confirm credentials"})

				