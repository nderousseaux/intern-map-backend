from flask import jsonify

from main import app
from data import get_data

@app.route("/", methods=["GET"])
def index():
	return jsonify({'message': 'Hello world!'}), 200

@app.route("/data", methods=["GET"])
def companies():
	return get_data()