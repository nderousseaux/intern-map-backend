import unittest
from main import app	

class TestRoot(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.result = self.app.get('/')

	def test_root_status_code(self):
		self.assertEqual(self.result.status_code, 200)
		
	def test_root_is_json(self):
		self.assertTrue(self.result.is_json)

	def test_root_has_message(self):
		self.assertTrue(self.result.json['message'])

	def test_root_message_is_string(self):
		self.assertIsInstance(self.result.json['message'], str)

	def test_root_message_is_hello_world(self):
		self.assertEqual(self.result.json['message'], 'Hello world!')
		

if __name__ == '__main__':
    unittest.main()