#!/usr/bin/python3
"""
This module creates the Flask application and handles setup.
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database session after each request.
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors and returns a JSON response.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
