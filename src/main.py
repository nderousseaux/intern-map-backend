# serveur flask

from companies import get_companies

from flask import Flask, request

app = Flask(__name__)

# CORS
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response

@app.route('/companies', methods=['GET'])
def companies():
	if request.method == 'GET':
		return get_companies()
		
@app.route('/', methods=['GET'])
def index():
	return "Hello world"
	
if __name__ == '__main__':
	app.run(debug=True, port=5001)