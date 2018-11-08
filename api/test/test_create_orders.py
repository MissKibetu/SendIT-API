import unittest
import json
from api.version1.all_orders import app

class TestOrders(unittest.TestCase):
	"""This class tests order creation"""
	def setUp(self):
		self.api = app
		self.client = self.api.test_client()

		self.new_order1 = {
			"sender_name" : "Jane Doe",
			"sender_email" : "janedoe@test.com",
			"pick_up" : "Nairobi",
			"drop_off" : "Mombasa",
			"recipient_name" : "John Doe",
			"weight" : 4,
			"cost" : 200,
			"status" : "Order requested"
		}
	"""Test order creation"""
	def test_create_order(self):
		result = self.client.post('/api/v1/create_order', data = json.dumps(self.new_order1), content_type='application/json')
		self.assertEqual(result.status_code, 201)