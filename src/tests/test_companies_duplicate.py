import unittest

from main import app	
from db import init_db

new_company = {
	"name": "Test Company",
	"address": "2 Rue du Cheval Blanc",
	"city": "Saint-Chéron",
	"zip": "91530",
	"tutor": "Test Tutor",
	"manager": "Test Manager",
	"phone": "123456789",
	"mail": "mail@mail.com",
	"website": "www.test.com",
	"gps": {
		"lat": 48.543307,
		"lng": 2.116364,
	},
}

class TestCompaniesDuplicate(unittest.TestCase):

	def setUp(self):
		# Create 2 new test company
		self.db = init_db()
		self.db.post(f"INSERT INTO company (name, address, city, zip, tutor, manager, phone, mail, web, latitude, longitude) VALUES ('{new_company['name']}', '{new_company['address']}', '{new_company['city']}', '{new_company['zip']}', '{new_company['tutor']}', '{new_company['manager']}', '{new_company['phone']}', '{new_company['mail']}', '{new_company['website']}', '{new_company['gps']['lat']}', '{new_company['gps']['lng']}')")
		self.db.post(f"INSERT INTO company (name, address, city, zip, tutor, manager, phone, mail, web, latitude, longitude) VALUES ('{new_company['name']}', '{new_company['address']}', '{new_company['city']}', '{new_company['zip']}', '{new_company['tutor']}', '{new_company['manager']}', '{new_company['phone']}', '{new_company['mail']}', '{new_company['website']}', '{new_company['gps']['lat']}', '{new_company['gps']['lng']}')")


		self.app = app.test_client()
		self.result = self.app.get('/data')
		self.companies = self.result.json['companies']
		self.tags = self.result.json['tags']

	def tearDown(self):
		# Delete the test company
		self.db.post(f"DELETE FROM company WHERE name='{new_company['name']}' and address='{new_company['address']}' and city='{new_company['city']}' and zip='{new_company['zip']}' and tutor='{new_company['tutor']}' and manager='{new_company['manager']}' and phone='{new_company['phone']}' and mail='{new_company['mail']}' and web='{new_company['website']}'")
		self.db.close

	def test_if_company_is_added(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['name'], new_company['name'])

	def test_if_company_has_no_duplicate(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']]
		self.assertEqual(len(company), 1)
		

if __name__ == '__main__':
    unittest.main()