import unittest
import json
from api import app
from api.db_config import cur, con, DbConfig

db = DbConfig()

class TestUsers(unittest.TestCase):

	def setUp(self):
		self.api = app
		self.client = self.api.test_client()

		self.valid_user ={
			"name": "Amy Lee",
			"email": "amylee@test.com",
			"password": "password",
			"confirm": "password",
			"role" : "user"
		}
		self.empty_fields ={
			"name": "Amy Lee",
			"email": "amylee@test.com",
			"password": "password",
			"confirm": ""
		}
		self.pasword_mismatch ={
			"name": "Amy Lee",
			"email": "amylee@test.com",
			"password": "password",
			"confirm": "passw"
		}
		
		self.valid_signin ={
			"email": "amylee@test.com",
			"password": "password"
		}
		self.invalid_password ={
			"email": "amylee@test.com",
			"password": "pass"
		}

		self.invalid_email ={
			"email": "amylee.com",
			"password": "password"
		}


	def test_valid_user_signup(self):
		result = self.client.post('/api/v2/signup', data = json.dumps(self.valid_user), content_type='application/json')
		self.assertEqual(result.status_code, 200)

	def test_empty_fields_signup(self):
		result = self.client.post('/api/v2/signup', data = json.dumps(self.empty_fields), content_type='application/json')
		self.assertIn("fields cannot be empty", str(result.data))

	def test_pasword_mismatch_signup(self):
		result = self.client.post('/api/v2/signup', data = json.dumps(self.pasword_mismatch), content_type='application/json')
		self.assertIn("please confirm your password", str(result.data)) 
	
	def test_valid_signin(self):
		result = self.client.post('/api/v2/signin', data = json.dumps(self.valid_signin), content_type='application/json')
		self.assertIn("Logged in", str(result.data)) 

	def test_invalid_password_signin(self):
		result = self.client.post('/api/v2/signin', data = json.dumps(self.invalid_password), content_type='application/json')
		self.assertIn("Invalid credentials. Please try again.", str(result.data)) 

	def test_invalid_email_signin(self):
		result = self.client.post('/api/v2/signin', data = json.dumps(self.invalid_email), content_type='application/json')
		self.assertIn("Invalid credentials. Please try again.", str(result.data)) 


 	