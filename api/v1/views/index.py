#!/usr/bin/python3
"""
Index view for HBNB API
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route("/status", strict_slashes=False, methods=["GET"])
def status():
    """return status for the api"""
    return {
        "status": "OK",
    }


@app_views.route("/stats", strict_slashes=False, methods=["GET"])
def stat():
    """return stats about each class"""
    amenities = storage.count(Amenity)
    cities = storage.count(City)
    places = storage.count(Place)
    reviews = storage.count(Review)
    states = storage.count(State)
    users = storage.count(User)
    return {
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users,
    }
# #!/usr/bin/python3
# """
# Index view for API
# """
# from api.v1.views import app_views
# from flask import jsonify
# from models import storage
#
#
# @app_views.route('/status', methods=['GET'], strict_slashes=False)
# def status():
#     """Return status of API"""
#     return jsonify({"status": "OK"}), 200
#
#
# @app_views.route('/stats', methods=['GET'], strict_slashes=False)
# def number_objects():
#     """Retrieves the number of each objects by type"""
#     classes = {
#         "amenities": storage.count("Amenity"),
#         "cities": storage.count("City"),
#         "places": storage.count("Place"),
#         "reviews": storage.count("Review"),
#         "states": storage.count("State"),
#         "users": storage.count("User")
#     }
#     return jsonify(classes), 200
# @app_views.route('/stats', methods=['GET'], strict_slashes=False)
# def number_objects():
#     """Retrieves the number of each objects by type"""
#     classes = {
#         "amenities": "Amenity",
#         "cities": "City",
#         "places": "Place",
#         "reviews": "Review",
#         "states": "State",
#         "users": "User"
#     }
#     for key, value in classes.items():
#         classes[key] = storage.count(value)
#     return jsonify(classes)
# """Index view"""
# from api.v1.views import app_views
# from flask import jsonify
# from models import storage
# from models.amenity import Amenity
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models.user import User
#
#
# @app_views.route('/status', methods=['GET'])
# def status():
#     """Return API status"""
#     return jsonify({"status": "OK"})
#
#
# @app_views.route('/stats', methods=['GET'])
# def stats():
#     """Retrieve the number of each objects by type"""
#     classes = {
#         "amenities": Amenity,
#         "cities": City,
#         "places": Place,
#         "reviews": Review,
#         "states": State,
#         "users": User
#     }
#
#     stats = {}
#     for key, cls in classes.items():
#         stats[key] = storage.count(cls)
#
#     return jsonify(stats)
