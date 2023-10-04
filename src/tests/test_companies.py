import unittest
from main import app	

class TestCompanies(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.result = self.app.get('/data')
		self.companies = self.result.json['companies']
		self.tags = self.result.json['tags']

	# Companies 
	def test_companies_is_dict(self):
		self.assertIsInstance(self.companies, dict)

	def test_companies_is_not_empty(self):
		self.assertTrue(self.companies)

	def test_companies_keys_are_int(self):
		for key in self.companies.keys():
			self.assertIsInstance(int(key), int)

	# One company
	def test_company_is_dict(self):
		for value in self.companies.values():
			self.assertIsInstance(value, dict)

	def test_company_is_not_empty(self):
		for value in self.companies.values():
			self.assertTrue(value)

	def test_company_keys_are_str(self):
		for value in self.companies.values():
			for key in value.keys():
				self.assertIsInstance(key, str)

	def test_company_has_11_keys(self):
		for value in self.companies.values():
			self.assertEqual(len(value.keys()), 11)

	# Test name
	def test_company_has_name(self):
		for value in self.companies.values():
			self.assertIn('name', value.keys())

	def test_company_name_is_str(self):
		for value in self.companies.values():
			self.assertIsInstance(value['name'], str)

	def test_company_name_is_not_empty(self):
		for value in self.companies.values():
			self.assertTrue(value['name'])
	
	# Test address
	def test_company_has_address(self):
		for value in self.companies.values():
			self.assertIn('address', value.keys())
	
	def test_company_address_is_str(self):
		for value in self.companies.values():
			self.assertIsInstance(value['address'], str)

	def test_company_address_is_not_empty(self):
		for value in self.companies.values():
			self.assertTrue(value['address'])

	# Test city
	def test_company_has_city(self):
		for value in self.companies.values():
			self.assertIn('city', value.keys())

	def test_company_city_is_str(self):
		for value in self.companies.values():
			self.assertIsInstance(value['city'], str)

	def test_company_city_is_not_empty(self):
		for value in self.companies.values():
			self.assertTrue(value['city'])

	# Test zip
	def test_company_has_zip(self):
		for value in self.companies.values():
			self.assertIn('zip', value.keys())
	
	def test_company_zip_is_str(self):
		for value in self.companies.values():
			self.assertIsInstance(str(value['zip']), str)
		
	# Test tutor
	def test_company_has_tutor(self):
		for value in self.companies.values():
			self.assertIn('tutor', value.keys())

	def test_company_tutor_is_str_or_null(self):
		for value in self.companies.values():
			self.assertTrue(value['tutor'] is None or isinstance(value['tutor'], str))

	# Test manager
	def test_company_has_manager(self):
		for value in self.companies.values():
			self.assertIn('manager', value.keys())

	def test_company_manager_is_str_or_null(self):
		for value in self.companies.values():
			self.assertTrue(value['manager'] is None or isinstance(value['manager'], str))

	# Test phone
	def test_company_has_phone(self):
		for value in self.companies.values():
			self.assertIn('phone', value.keys())

	def test_company_phone_is_str_or_null(self):
		for value in self.companies.values():
			self.assertTrue(value['phone'] is None or isinstance(value['phone'], str))

	# Test email
	def test_company_has_email(self):
		for value in self.companies.values():
			self.assertIn('mail', value.keys())

	def test_company_email_is_str_or_null(self):
		for value in self.companies.values():
			self.assertTrue(value['mail'] is None or isinstance(value['mail'], str))

	# Test website
	def test_company_has_website(self):
		for value in self.companies.values():
			self.assertIn('website', value.keys())

	def test_company_website_is_str_or_null(self):
		for value in self.companies.values():
			self.assertTrue(value['website'] is None or isinstance(value['website'], str))

	
	# Test gps
	def test_company_has_gps(self):
		for value in self.companies.values():
			self.assertIn('gps', value.keys())

	def test_company_gps_is_dict(self):
		for value in self.companies.values():
			self.assertIsInstance(value['gps'], dict)

	def test_company_gps_has_lat(self):
		for value in self.companies.values():
			self.assertIn('lat', value['gps'].keys())

	def test_company_gps_has_lng(self):
		for value in self.companies.values():
			self.assertIn('lng', value['gps'].keys())

	def test_company_gps_lat_is_not_empty(self):
		for value in self.companies.values():
			self.assertTrue(value['gps']['lat'])

	def test_company_gps_lng_is_not_empty(self):
		for value in self.companies.values():
			self.assertTrue(value['gps']['lng'])

	def test_company_gps_lat_is_float(self):
		for value in self.companies.values():
			self.assertIsInstance(value['gps']['lat'], float)

	def test_company_gps_lng_is_float(self):
		for value in self.companies.values():
			self.assertIsInstance(value['gps']['lng'], float)

	
	# Test tags
	def test_company_has_tags(self):
		for value in self.companies.values():
			self.assertIn('tags', value.keys())

	def test_company_tags_is_list(self):
		for value in self.companies.values():
			self.assertIsInstance(value['tags'], list)

	def test_company_tags_is_int(self):
		for value in self.companies.values():
			for tag in value['tags']:
				self.assertIsInstance(tag, int)

	def test_company_tags_no_duplicates(self):
		for value in self.companies.values():
			self.assertEqual(len(value['tags']), len(set(value['tags'])))

	def test_company_tags_exist_in_tags(self):
		for value in self.companies.values():
			for tag in value['tags']:
				self.assertIn(str(tag), self.tags.keys())



if __name__ == '__main__':
    unittest.main()