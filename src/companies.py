from flask import jsonify

def get_companies():
	return jsonify({ "msg": "Hello World" })