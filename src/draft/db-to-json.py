import mysql.connector as mysql
import json

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

# On récupère toutes les données de la table tag
c.execute("SELECT * FROM tag")
tags = c.fetchall()

# On récupère toutes les données de la table company_tag
c.execute("SELECT * FROM company_tag")
company_tags = c.fetchall()

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
for company_tag in company_tags:
	companies_dict[company_tag[0]]["tags"].append(company_tag[1])

# On crée le dictionnaire complet
output = {
	"companies": companies_dict,
	"tags": tags_dict,
}


# On exporte le dictionnaire au format JSON
with open("data.json", "w") as f:
	json.dump(output, f, indent=2)



# On ferme tout
c.close()
mysql.close()