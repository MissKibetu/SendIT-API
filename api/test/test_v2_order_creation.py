import unittest
import json
from api import app
from api.db_config import cur, con, DbConfig

db = DbConfig()

class TestOrderCreation(unittest.TestCase):
	def setUp(self):
		self.api = app
		self.client = self.api.test_client()
	
	
		self.valid_order = {
			"sender_name": "Amy Lee",
			"sender_email": "amylee@test.com",
			"pick_up": "Machakos",
			"drop_off": "Meru",
			"recipient_name" : "Jacky Lee",
			"weight" : 4, 
			"cost": 200,
			"status": "Order requested",
			"current_location": "Machakos"
		}
		self.empty_field_order = {
			"sender_name": "Amy Lee",
			"sender_email": "amylee@test.com",
			"pick_up": "",
			"drop_off": "Meru",
			"recipient_name" : "Jacky Lee",
			"weight" : 4, 
			"cost": 200,
			"status": "Order requested",
			"current_location": "Machakos"
		}
		self.invalid_weight = {
			"sender_name": "Amy Lee",
			"sender_email": "amylee@test.com",
			"pick_up": "Machakos",
			"drop_off": "Meru",
			"recipient_name" : "Jacky Lee",
			"weight" : 0, 
			"cost": 200,
			"status": "Order requested",
			"current_location": "Machakos"
		}

	def test_valid_order(self):
		result = self.client.post('/api/v2/order_request/amylee@test.com', data = json.dumps(self.valid_order), content_type='application/json')
		self.assertEqual(result.status_code, 201)
		self.assertIn("Order created", str(result.data))

	def test_empty_field_order(self):
		result = self.client.post('/api/v2/order_request/amylee@test.com', data = json.dumps(self.empty_field_order), content_type='application/json')
		self.assertIn("fields cannot be empty", str(result.data))

	def test_invalid_weight(self):
		result = self.client.post('/api/v2/order_request/amylee@test.com', data = json.dumps(self.invalid_weight), content_type='application/json')
		self.assertIn("weight cannot be zero", str(result.data))

	def test_invalid_email(self):
		result = self.client.post('/api/v2/order_request/amyl@test.com', data = json.dumps(self.valid_order), content_type='application/json')
		self.assertIn("email not registered", str(result.data))
