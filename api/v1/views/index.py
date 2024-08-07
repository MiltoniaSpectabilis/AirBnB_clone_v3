#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """Return API status"""
    return {
        "status": "OK",
    }


@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieve the number of each objects by type"""
    classes = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }

    stats = {}
    for key, cls in classes.items():
        stats[key] = storage.count(cls)

    return jsonify(stats)