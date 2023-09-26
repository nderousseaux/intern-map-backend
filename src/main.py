# serveur flask

from companies import get_companies

from flask import Flask, request

app = Flask(__name__)

@app.route('/companies', methods=['GET'])
def companies():
	if request.method == 'GET':
		return get_companies()
		
	
if __name__ == '__main__':
	app.run(debug=True)