#!/usr/bin/python3
"""
Flask Application
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 Error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
# from flask import Flask, jsonify, make_response
# from models import storage
# from api.v1.views import app_views
# import os
# from flask_cors import cors
#
# app = Flask(__name__)
# app.register_blueprint(app_views)
# CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
#
#
# @app.teardown_appcontext
# def close_db(error):
#     """Close Storage"""
#     storage.close()
#
#
# @app.errorhandler(404)
# def not_found(error):
#     """404 Error"""
#     return make_response(jsonify({"error": "Not found"}), 404)
#
#
# if __name__ == "__main__":
#     host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
#     port = int(os.environ.get('HBNB_API_PORT', 5000))
#     app.run(host=host, port=port, threaded=True)
