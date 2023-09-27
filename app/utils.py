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
	db_host = getenv('DB_HOST')
	db_user = getenv('DB_USER')
	db_passwd = getenv('DB_PASSWD')
	db_database = getenv('DB_DATABASE')

	load_dotenv()
	if db_host is None:
		print("DB_HOST is None")
		db_host = getenv('DB_HOST')
		print(db_host)
	if db_user is None:
		db_user = getenv('DB_USER')
	if db_passwd is None:
		db_passwd = getenv('DB_PASSWD')
	if db_database is None:
		db_database = getenv('DB_DATABASE')


	db = DB(db_host, db_user, db_passwd, db_database)
	db.connect()
	db.get_cursor()
	return db