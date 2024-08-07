#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views
from flask import jsonify


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
