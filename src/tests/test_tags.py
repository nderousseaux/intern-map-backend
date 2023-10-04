import unittest
from main import app	

class TestTags(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.result = self.app.get('/data')
		self.tags = self.result.json['tags']

	def test_tags_is_dict(self):
		self.assertIsInstance(self.tags, dict)

	def test_tags_is_not_empty(self):
		self.assertTrue(self.tags)

	def test_tags_keys_are_int(self):
		for key in self.tags.keys():
			self.assertIsInstance(int(key), int)

	def test_tags_values_are_dict(self):
		for value in self.tags.values():
			self.assertIsInstance(value, dict)

	def test_tags_values_are_not_empty(self):
		for value in self.tags.values():
			self.assertTrue(value)

	def test_tags_values_keys_are_str(self):
		for value in self.tags.values():
			for key in value.keys():
				self.assertIsInstance(key, str)

	def test_tags_values_one_key(self):
		for value in self.tags.values():
			self.assertEqual(len(value.keys()), 1)

	def test_tags_values_key_is_name(self):
		for value in self.tags.values():
			self.assertIn('name', value.keys())

	def test_tags_values_name_is_str(self):
		for value in self.tags.values():
			self.assertIsInstance(value['name'], str)


if __name__ == '__main__':
    unittest.main()