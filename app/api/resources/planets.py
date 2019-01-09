""" This resource is the entry endpoint for the API.
This just returns information about the API and the creator.
"""

from flask import (jsonify, request)
from flask_restful import Resource
from bson.objectid import ObjectId
from app.api.utils.messages import (error_message, success_message)

from app.api.extensions import (MONGO, SWAPI)


class Planet(Resource):
    """ Class that contains all methods used in the API regarding the planets
    Inherits from Resource to use advantage of flask_restful power.
    """

    @staticmethod
    def transform_data(data: dict)->dict:
        """Function to return the data humanized, getting the apparitionsCount
        of the planet on moviesand casts ObjectId to str.

        Arguments:
            data {dict} -- [description]

        Returns:
            dict -- [description]
        """
        return {
            "id": str(data['_id']),
            "name": data['name'],
            "climate": data['climate'],
            "terrain": data['terrain'],
            "apparitionsCount": SWAPI.get_planet(data['name'])
            }

    @staticmethod
    def get(planet_id=None, planet_name=None)->jsonify:
        """GET HTTP Verb for the Planets. This returns a list if no parameter,
        or information about a specific planet using planet id or planet name.

        Returns:
            jsonify -- A jsonified object from a dict holding
                        a planet info.
        """
        data = list()


        if planet_id:
            planet = MONGO.db.planets.find_one({"_id": ObjectId(planet_id)})
            if planet:
                data.append(Planet.transform_data(planet))
        elif planet_name:
            planet = MONGO.db.planets.find_one({"name": planet_name})
            if planet:
                data.append(Planet.transform_data(planet))
        else:
            for planet in MONGO.db.planets.find():
                data.append(Planet.transform_data(planet))

        if data == 0:
            return success_message(204, data)

        return jsonify(data)

    @staticmethod
    def post()->jsonify:
        """Threats requisitions from POST HTTP Verb.
        It's used to insert new planets on the database as long as
        they exists on StarWars API

        Returns:
            jsonify -- A JSON with the code of the operation status and,
            if data was inserted, the planet details
        """
        data = request.get_json()

        if not data:
            return error_message(422, 'No data to insert.') # Unprocessable Entity

        if MONGO.db.planets.find_one({"name": data.get('name')}):
            return error_message(409, 'This planet already exists.') # Conflict

        planet_apparitions = SWAPI.set_planet(data.get('name'))

        if not planet_apparitions:
            return error_message(403,
                                 'This planet was not found on StarWars API.') # Prohibited

        inserted = MONGO.db.planets.insert(data)
        inserted = MONGO.db.planets.find_one({"_id": ObjectId(inserted)})

        return success_message(201, Planet.transform_data(inserted))


    @staticmethod
    def put(planet_id: str = None)->jsonify:
        """Threats requisitions from PUT HTTP Verb.
        It's used to insert new planets on the database as long as
        they exists on StarWars API

        Returns:
            jsonify -- A JSON with the code of the operation status and,
            if data was inserted, the planet details
        """
        data = request.get_json()
        if not data or not planet_id:
            return error_message(422, 'No planet id or data to update.') # Unprocessable Entity

        if not MONGO.db.planets.find_one({"_id": ObjectId(planet_id)}):
            return error_message(204, 'Planet id didn\'t find')

        updated = MONGO.db.planets.update({'_id': ObjectId(planet_id)}, {'$set': data})
        updated = MONGO.db.planets.find_one({"_id": ObjectId(planet_id)})

        return success_message(200, Planet.transform_data(updated))



    @staticmethod
    def delete(planet_id: str = None, planet_name: str = None)->jsonify:
        """Threats requisitions from DELETE HTTP Verb.
        It's used to delete a planet on the database based on it's id
        or name.

        Returns:
            jsonify -- A JSON with the code of the operation status.
        """
        if planet_id:
            MONGO.db.planets.remove({'_id': ObjectId(planet_id)})
        elif planet_name:
            MONGO.db.planets.remove({'name': planet_name})
        else:
            return error_message(422, 'No planet id or planet name to delete')

        return success_message(204, list())
