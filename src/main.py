from flask import Flask


app = Flask("Internmap")

# Configuration from config.py (CORS request)
from config import *

# All routes are in routes.py
from routes import *

if __name__ == "__main__":
		app.run(debug=True, port=5001)