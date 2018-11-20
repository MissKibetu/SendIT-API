from api import app
from api.db_config import con, cur, url, psycopg2
from flask import request,jsonify
from passlib.hash import sha256_crypt
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from api.v2.validations.models import Validations

validationObject = Validations()

class User():

	""" User Registration. Default role set to user """

	def user_signup(self):
		name = request.json['name']
		email = request.json['email']
		password = request.json['password']  	
		confirm = request.json['confirm']
		role = "user"

		if any(user_input == "" for user_input in (name, email, password, confirm)):
			return {"message" : "fields cannot be empty"}
		
		if password!=confirm:
			return "please confirm your password"

		email_check = validationObject.email_check(email)

		if email_check:
			return "This email is already registered."
		
		
		password = sha256_crypt.encrypt(str(password))
		cur.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)", (name, email, password, role))
		con.commit()
		return ("Welcome " + name + ". You have been registered to SendIT" )

	
	
	def user_login(self):

		""" User Login. Redirect Admin and Customers to different pages.  """

		email = request.json['email']
		password = str(request.json['password'] )
		email_check = validationObject.email_check(email)

		if email_check:
			user_password = cur.execute ("SELECT password FROM users WHERE email = %s", ([email]))
			user_password = cur.fetchone()[0]

			if sha256_crypt.verify(password, user_password):
				role_check = validationObject.role_check(email)
				access_token = create_access_token(identity = email)
				if role_check == "admin":
					return jsonify({'message': 'Welcome to the admin page. Access token = ' + access_token})

				return jsonify({'message': 'Logged in as: ' + email + ". Access token = " + access_token})


			return "Invalid credentials. Please try again."

		return "Invalid credentials. Please try again."

	

	def admin_account(self, email1):

		""" Change user role to admin """

		email2 = request.json['email']
		email_check = validationObject.email_check(email1)
		email_check2 = validationObject.email_check(email2)
		
		if email_check:
			role_check = validationObject.role_check(email1)
			role = "admin"

			if role_check == role:
				if email_check2:
					role_check2 = validationObject.role_check(email2)
					
					if role_check2 != role:
						cur.execute("UPDATE users SET role = (%s) WHERE email = (%s)", (role, email2))
						con.commit()
						return (email2 + " role changed to admin")

					return (email2 + " is already admin")

				return "This email is unregistered."
	
			return "Admin rights required. You are not authorized to change user roles"
					
		return "You are not a registered user. Please confirm credentials"

		