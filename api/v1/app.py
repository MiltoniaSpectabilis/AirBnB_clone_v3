#!/usr/bin/python3
"""
This module creates the Flask application and handles setup.
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database session after each request.
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
# #!/usr/bin/python3
# """
# Flask Application
# """
# from flask import Flask, jsonify
# from models import storage
# from api.v1.views import app_views
# import os
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
# app.register_blueprint(app_views, url_prefix="/api/v1")
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     """this views handles 404 responses"""
#     return jsonify({"error": "Not found"}), 404
#
#
# @app.errorhandler(400)
# def page_not_found_400(e):
#     """this views handles 400 responses"""
#     message = e.description
#     return message, 400
#
#
# @app.teardown_appcontext
# def close(ctx):
#     """this view closes the database after each response"""
#     storage.close()
#
#
# if os.getenv("HBNB_API_HOST"):
#     host = os.getenv("HBNB_API_HOST")
# else:
#     host = "0.0.0.0"
#
# if os.getenv("HBNB_API_PORT"):
#     port = int(os.getenv("HBNB_API_PORT"))
# else:
#     port = 5000
#
#
# if __name__ == "__main__":
#     app.run(host=host, port=port, threaded=True)
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
