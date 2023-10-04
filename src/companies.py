from flask import jsonify
import requests

from db import init_db
from utils import get_env

CLE_GEOCODING = get_env("GEOCODING_API_KEY")

def get_companies():
	"""Return a list of companies and tags.
	This will be in 3 steps :
	1. Get all companies from database.
	2. Check if data is clean (lat/lng, not duplicate, etc...)
				If is not, clean data.
	3. Return all companies and tags.
	"""

	db = init_db()

	# First step : get all companies from database
	companies, tags, companies_tags = get_data_from_db(db)

	# Second step : correct possible problems in data
	companies, companies_tags = clean_data(db, companies, companies_tags)

	db.close()

	# Third step : return all companies
	return format_data(companies, tags, companies_tags)

def get_data_from_db(db):
	""" Get all companies from database.
	3 tables are used :
	- company
	- tag
	- company_tag
	"""

	companies = db.get("SELECT * FROM company")
	tags = db.get("SELECT * FROM tag")
	companies_tags = db.get("SELECT * FROM company_tag")

	return companies, tags, companies_tags

def clean_data(db, companies, companies_tags):
	""" Check if data is clean (lat/lng, not duplicate, etc...)
	2 steps :
	- Check if lat/lng is correct. If not, use geocode API to get lat/lng and save to database.
	- Check if companies have duplicate. If yes, delete duplicate.
	"""

	companies = check_lat_lng(db, companies)

	companies, companies_tags = check_duplicate(db, companies, companies_tags)
	
	return companies, companies_tags

def check_lat_lng(db, companies):
	""" Check if lat/lng is correct. If not, use geocode API to get lat/lng and save to database.
	"""

	edit = False

	# Looking for companies without lat/lng (companies[10] = lat, companies[11] = lng)
	companies_to_correct = [company for company in companies if company[10] == None or company[11] == None]

	# For each company without lat/lng, use geocode API to get lat/lng and save to database
	for company in companies_to_correct:

		# Get address from company
		address = f"{company[2]} {company[3]} {company[4]}"

		# Get lat/lng from geocode API
		url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={CLE_GEOCODING}"
		response = requests.get(url)
		
		# Check if response is OK
		if response.status_code != 200:
			continue

		# Get lat/lng from response
		data = response.json()

		# Edit company with lat/lng
		lat = data["results"][0]["geometry"]["location"]["lat"]
		lng = data["results"][0]["geometry"]["location"]["lng"]

		edit = True
		db.post(f"UPDATE company SET latitude={lat}, longitude={lng} WHERE id={company[0]}")

	if edit:
		# Regenerate companies
		companies = db.get("SELECT * FROM company")

	return companies

def check_duplicate(db, companies, companies_tags):
	""" Check if companies have duplicate. If yes, delete duplicate.
	"""

	edit = False

	# Verify if companies have same lat and lng
	for company in companies:
		companies_to_delete = []
		for company_to_compare in companies:
			if company[0] == company_to_compare[0]:
				continue
			if company[10] == company_to_compare[10] and company[11] == company_to_compare[11]:
				companies_to_delete.append(company_to_compare)

		if len(companies_to_delete) > 0:
			companies_to_delete.append(company)
			
			# Delete duplicate, keep only one with the greatest id
			companies_to_delete.sort(key=lambda x: x[0])
			companies_to_delete.pop()

			for company_to_delete in companies_to_delete:
				edit = True
				db.post(f"DELETE FROM company_tag WHERE company_id={company_to_delete[0]}")
				db.post(f"DELETE FROM company WHERE id={company_to_delete[0]}")

	if edit:
				
		# Regenerate companies
		companies = db.get("SELECT * FROM company")
		# Regenerate companies_tags
		companies_tags = db.get("SELECT * FROM company_tag")
	
	return companies, companies_tags

def format_data(companies, tags, companies_tags):
	""" Format companies, tags and companies_tag to return a JSON.
	Return 2 dict : companies and tags.
	"""

	# Dict for companies
	companies_return = {}
	for company in companies:
		companies_return[company[0]] = {
			"name": company[1],
			"address": company[2],
			"city": company[3],
			"zip": company[4],
			"phone": company[5],
			"mail": company[6],
			"website": company[7],
			"manager": company[8],
			"tutor": company[9],
			"gps": {
				"lat": float(company[10]),
				"lng": float(company[11]),
			},
			"tags": [],
		}

	# Dict for tags
	tags_return = {}
	for tag in tags:
		tags_return[tag[0]] = {
			"name": tag[1],
		}

	# Add tags to companies
	for company_tag in companies_tags:
		companies_return[company_tag[0]]["tags"].append(company_tag[1])

	
	# Dict for all
	output = {
		"companies": companies_return,
		"tags": tags_return,
	}

	return jsonify(output), 200