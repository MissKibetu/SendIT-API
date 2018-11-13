import unittest
import json
from api.version1.orders import app

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

		self.new_order2 = {
			"sender_name" : "",
			"sender_email" : "janedoe@test.com",
			"pick_up" : "Nairobi",
			"drop_off" : "Mombasa",
			"recipient_name" : "John Doe",
			"weight" : 4,
			"cost" : 200,
			"status" : "Order requested"
		}

		self.new_order3 = {
			"sender_name" : "Jane Doe",
			"sender_email" : "janedoe@test.com",
			"pick_up" : "Nairobi",
			"drop_off" : "Mombasa",
			"recipient_name" : "John Doe",
			"weight" : 0
		}

	"""Test order creation"""
	def test_create_order(self):
		result = self.client.post('/api/v1/create_order', data = json.dumps(self.new_order1), content_type='application/json')
		self.assertEqual(result.status_code, 201)

	def test_create_order2(self):
		result = self.client.post('/api/v1/create_order', data = json.dumps(self.new_order2), content_type='application/json')
		self.assertEqual(result.status_code, 201)

	def test_create_order3(self):
		result = self.client.post('/api/v1/create_order', data = json.dumps(self.new_order3), content_type='application/json')
		self.assertEqual(result.status_code, 201) 