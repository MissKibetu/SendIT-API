import unittest
import json
from api.version1.all_orders import app

class TestOrders(unittest.TestCase):
	"""This class tests the fetching of orders"""
	def setUp(self):
		self.api = app
		self.client = self.api.test_client()

		"""Sample Order ist"""

		self.order1 ={
				"parcelID" : 1,
				"sender_name" : "Jane Doe",
				"sender_email" : "janedoe@test.com",
				"pick_up" : "Nairobi",
				"drop_off" : "Mombasa",
				"recipient_name" : "John Doe",
				"weight" : 4,
				"cost" : 200,
				"status" : "Delivered"
			}

		self.order2 = {
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
	
	"""Test cancel order for ID that exists and status ==delivered"""
	def test_cancel_orders_1(self):
		result = self.client.put('/api/v1/cancel/1', data = json.dumps(self.order1), content_type='application/json')
		self.assertEqual(result.status_code, 200)

	"""Test cancel order for ID that exists and status !=delivered """
	def test_cancel_orders_2(self):
		result = self.client.put('/api/v1/cancel/2', data = json.dumps(self.order2), content_type='application/json')
		self.assertEqual(result.status_code, 200)

	"""Test cancel order for ID that does not exist """
	def test_cancel_orders_3(self):
		result = self.client.put('/api/v1/cancel/3', data = json.dumps(self.order2), content_type='application/json')
		self.assertEqual(result.status_code, 200)