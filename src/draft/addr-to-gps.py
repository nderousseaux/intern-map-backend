import mysql.connector as mysql
import requests

CLE_GEOCODING = "YOUR_API_KEY"

# Connect to MySQL
mysql = mysql.connect(
		host="localhost",
		user="user",
		passwd="password",
		database="db",
		)

# Create cursor
c = mysql.cursor()

# On récupère toutes les données de la table company
c.execute("SELECT * FROM company")
companies = c.fetchall()

# Pour chaque compagnie, on récupère l'adresse
for company in companies:
	addr = f"{company[2]} {company[3]} {company[4]}"

	# On fait une requete à l'API de Google Maps pour récupérer les coordonnées GPS
	url = f"https://maps.googleapis.com/maps/api/geocode/json?address={addr}&key={CLE_GEOCODING}"
	response = requests.get(url)
	data = response.json()

	# On récupère les coordonnées GPS
	lat = data["results"][0]["geometry"]["location"]["lat"]
	lng = data["results"][0]["geometry"]["location"]["lng"]

	# On met à jour la table company
	c.execute(f"UPDATE company SET latitude={lat}, longitude={lng} WHERE id={company[0]}")

# On commit
mysql.commit()




# On ferme tout
c.close()
mysql.close()