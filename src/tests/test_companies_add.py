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
}
lat = 48.543307
lng = 2.116364

class TestCompaniesAdd(unittest.TestCase):

	def setUp(self):
		# Create a new test company
		self.db = init_db()
		self.db.post(f"INSERT INTO company (name, address, city, zip, tutor, manager, phone, mail, web) VALUES ('{new_company['name']}', '{new_company['address']}', '{new_company['city']}', '{new_company['zip']}', '{new_company['tutor']}', '{new_company['manager']}', '{new_company['phone']}', '{new_company['mail']}', '{new_company['website']}')")

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

	def test_if_company_has_correct_address(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['address'], new_company['address'])

	def test_if_company_has_correct_city(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['city'], new_company['city'])

	def test_if_company_has_correct_zip(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['zip'], new_company['zip'])
	
	def test_if_company_has_correct_tutor(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['tutor'], new_company['tutor'])

	def test_if_company_has_correct_manager(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['manager'], new_company['manager'])

	def test_if_company_has_correct_phone(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['phone'], new_company['phone'])

	def test_if_company_has_correct_mail(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['mail'], new_company['mail'])

	def test_if_company_has_correct_website(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(company['website'], new_company['website'])

	def test_if_company_has_correct_gps_lat(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(float(company['gps']['lat']), lat)	

	def test_if_company_has_correct_gps_lng(self):
		company = [company for company in self.companies.values() if company['name'] == new_company['name']][0]
		self.assertEqual(float(company['gps']['lng']), lng)

if __name__ == '__main__':
    unittest.main()