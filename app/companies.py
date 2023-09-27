from os import getenv

from flask import jsonify
import requests
from dotenv import load_dotenv

from utils import get_db

# getting from .env file 'GEOCODING_API'
CLE_GEOCODING=getenv("GEOCODING_API_KEY")
if CLE_GEOCODING is None:
	load_dotenv()
	CLE_GEOCODING=getenv("GEOCODING_API")

def get_companies():
	""" GET /companies
	3 step.
	First, get all companies from database.
	Second, check if companies have lat/lng. If not, use geocode to get lat/lng and save to database.
	Third, return all companies with this format :
	{
		"companies": {
			"1502": {
				"name": "NATTER  ELECTRICITE",
				"address": "Rue de la Tuilerie ",
				"city": " ASPACH LE BAS",
				"zip": "68700",
				"phone": "0607769021",
				"mail": null,
				"website": null,
				"manager": "NATTER",
				"tutor": "ZIEGLER MICHEL",
				"gps": {
					"lat": 47.767928,
					"lng": 7.140398
				},
				"tags": [
					20
				]
			},
			...
		},
		"tags": {
			"19": {
				"name": "ASSP"
			},
			...
		}
  }
	"""

	# First step : get all companies from database
	db, companies, tags, companies_tags = get_companies_from_database()

	# Second step : check if companies have lat/lng. If not, use geocode to get lat/lng and save to database.
	companies = add_lat_lng(db, companies)

	# Third step : return all companies
	return format_companies(companies, tags, companies_tags)

def get_companies_from_database():
	# Connect to database
	db = get_db()

	db.c.execute("SELECT * FROM company")
	companies = db.c.fetchall()

	db.c.execute("SELECT * FROM tag")
	tags = db.c.fetchall()

	# On récupère toutes les données de la table company_tag
	db.c.execute("SELECT * FROM company_tag")
	company_tags = db.c.fetchall()

	return db, companies, tags, company_tags


# check if companies have lat/lng. If not, use geocode to get lat/lng and save to database
def add_lat_lng(db, companies):
	for company in [company for company in companies if company[10] == None or company[11] == None]:
		addr = f"{company[2]} {company[3]} {company[4]}"
		
		# On fait une requete à l'API de Google Maps pour récupérer les coordonnées GPS
		url = f"https://maps.googleapis.com/maps/api/geocode/json?address={addr}&key={CLE_GEOCODING}"
		response = requests.get(url)
		data = response.json()

		print(data)

		# On récupère les coordonnées GPS
		lat = data["results"][0]["geometry"]["location"]["lat"]
		lng = data["results"][0]["geometry"]["location"]["lng"]


		# On met à jour la table company
		db.c.execute(f"UPDATE company SET latitude={lat}, longitude={lng} WHERE id={company[0]}")
		db.mysql.commit()

	# On récupère toutes les données de la table company
	db.c.execute("SELECT * FROM company")
	companies = db.c.fetchall()
	

	return companies
		
# Third step : return all companies
def format_companies(companies, tags, companies_tags):
	# On crée le dictionnaire des compagnies
	companies_dict = {}
	for company in companies:
		companies_dict[company[0]] = {
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

	# On crée le dictionnaire des tags
	tags_dict = {}
	for tag in tags:
		tags_dict[tag[0]] = {
			"name": tag[1],
		}

	# On ajoute les tags aux compagnies
	for company_tag in companies_tags:
		companies_dict[company_tag[0]]["tags"].append(company_tag[1])

	# On crée le dictionnaire complet
	output = {
		"companies": companies_dict,
		"tags": tags_dict,
	}

	return jsonify(output)
