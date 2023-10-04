from flask import jsonify

from main import app
from companies import get_companies

@app.route("/", methods=["GET"])
def index():
	return jsonify({'message': 'Hello world!'}), 200

@app.route("/companies", methods=["GET"])
def companies():
	return get_companies()