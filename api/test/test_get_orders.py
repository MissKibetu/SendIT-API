import unittest
import json
from api.version1.orders import app

class TestOrders(unittest.TestCase):
	"""This class tests the fetching of orders"""
	
	def setUp(self):
		self.api = app
		self.client = self.api.test_client()

		"""Sample Order ist"""

		self.orders_list = [
			{
				"parcelID" : 1,
				"sender_name" : "Jane Doe",
				"sender_email" : "janedoe@test.com",
				"pick_up" : "Nairobi",
				"drop_off" : "Mombasa",
				"recipient_name" : "John Doe",
				"weight" : 4,
				"cost" : 200,
				"status" : "Delivered"
			},
			{
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
		]  

	"""Test get all orders"""

	def test_get_all_orders(self):
		result = self.client.get('/api/v1/all_orders', data = json.dumps(self.orders_list), content_type='application/json')
		self.assertEqual(result.status_code, 200)

	"""Test get orders by parcelID"""

	def test_get_order_by_ID(self):
		result = self.client.get('/api/v1/all_orders/1', data = json.dumps(self.orders_list), content_type='application/json')
		self.assertEqual(result.status_code, 200)

	"""Test to check that a message is returned if the parcelID does not exist"""
	
	def test_nonexistent_ID(self):
		result = self.client.get('/api/v1/all_orders/4', data = json.dumps(self.orders_list), content_type='application/json')
		self.assertEqual(result.status_code, 200)
		self.assertIn("No orders with that ID", str(result.data))

	"""Test get orders by sender email"""
	
	def test_get_all_orders_by_sender_email(self):
		result = self.client.get('/api/v1/all_orders/johndoe@test.com', data = json.dumps(self.orders_list), content_type='application/json')
		self.assertEqual(result.status_code, 200)

	"""Test to check that a message is returned if the email does not exist"""
	
	def test_nonexistent_sender_email_2(self):
		result = self.client.get('/api/v1/all_orders/jacky@test.com', data = json.dumps(self.orders_list), content_type='application/json')
		self.assertEqual(result.status_code, 200)
		self.assertIn("No orders made from that email address", str(result.data))
		