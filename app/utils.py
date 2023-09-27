import mysql.connector as mysql
from dotenv import load_dotenv
from os import getenv
class DB:

	def __init__(self, host, user, passwd, database):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.database = database

	def connect(self):
		self.mysql = mysql.connect(
			host=self.host,
			user=self.user,
			passwd=self.passwd,
			database=self.database,
			)
	
	def get_cursor(self):
		self.c = self.mysql.cursor()
		return self.c

	def close(self):
		self.c.close()
		self.mysql.close() 



def get_db(): #TODO: variable d'environnement
	load_dotenv()
	print(getenv('DB_HOST'))
	print(getenv('DB_USER'))
	print(getenv('DB_PASSWD'))
	print(getenv('DB_DATABASE'))
	db = DB(getenv('DB_HOST'), getenv('DB_USER'), getenv('DB_PASSWD'), getenv('DB_DATABASE'))
	db.connect()
	db.get_cursor()
	return db