import unittest
from main import app	

class TestData(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.result = self.app.get('/data')

	def test_data_status_code(self):
		self.assertEqual(self.result.status_code, 200)
		
	def test_data_is_json(self):
		self.assertTrue(self.result.is_json)

	def test_data_has_companies(self):
		self.assertTrue(self.result.json['companies'])

	def test_data_has_tags(self):
		self.assertTrue(self.result.json['tags'])

if __name__ == '__main__':
    unittest.main()