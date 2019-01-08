""" This resource is the entry endpoint for the API.
This just returns information about the API and the creator.
"""

from flask_restful import Resource
from flask import jsonify

class Index(Resource):
    """ Class that contains all methods used in the index path of API
    Inherits from Resource to use advantage of flask_restful power.
    """

    @staticmethod
    def get()->jsonify:
        """GET HTTP Verb for the Index (root from api)

        Returns:
            jsonify -- A jsonified object from a dict holding
                        this API info.
        """
        info = {
            "name": "Star Wars B2W Challenge",
            "author": "Raphael Sathler",
            "webpage": "www.raphaelsathler.tk",
            "email": "sathler93@gmail.com",
            "license": "GNU GPL v3.0",
            }

        return jsonify(info)
