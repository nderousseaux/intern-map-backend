import mysql.connector as mysql

from utils import get_env

class DB:
	""" Class to model a database connection
	"""

	def __init__(self, host, user, passwd, database):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.database = database
		self.is_connected = False

	def connect(self):
		self.mysql = mysql.connect(
			host=self.host,
			user=self.user,
			passwd=self.passwd,
			database=self.database,
			)
		self.is_connected = True
	
	def get_cursor(self):
		self.c = self.mysql.cursor()
		return self.c
	
	def close(self):
		self.c.close()
		self.mysql.close()


	def get(self, query):
		if not self.is_connected:
			self.connect()

		if not hasattr(self, 'c'):
			self.get_cursor()

		self.c.execute(query)

		return self.c.fetchall()
	
	def post(self, query):
		if not self.is_connected:
			self.connect()

		if not hasattr(self, 'c'):
			self.get_cursor()

		self.c.execute(query)
		self.mysql.commit()


def init_db():
	""" Initialize database connection
	"""
	db_host = get_env("DB_HOST")
	db_user = get_env("DB_USER")
	db_passwd = get_env("DB_PASSWD")
	db_database = get_env("DB_DATABASE")

	db = DB(db_host, db_user, db_passwd, db_database)
	return db