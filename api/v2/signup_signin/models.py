from api import app
from api.db_config import con, cur, url, psycopg2
from flask import request,jsonify
from passlib.hash import sha256_crypt
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

	""" User Login. Redirect Admin and Customers to different pages.  """
	
	def user_login(self):
		email = request.json['email']
		password = str(request.json['password'] )
		email_check = validationObject.email_check(email)

		if email_check:
			user_password = cur.execute ("SELECT password FROM users WHERE email = %s", ([email]))
			user_password = cur.fetchone()[0]

			if sha256_crypt.verify(password, user_password):
				role_check = validationObject.role_check(email)

				if role_check == "admin":
					return ("Welcome to the admin page. User your power wisely!")

				return ("Logged in as: " + email)

			return "Invalid credentials. Please try again."

		return "Invalid credentials. Please try again."