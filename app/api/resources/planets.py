""" This resource is the entry endpoint for the API.
This just returns information about the API and the creator.
"""

from flask import (jsonify, request, url_for, redirect)
from flask_restful import Resource
from bson.objectid import ObjectId
from app.api.utils.error_messages import error_message

from app.api.extensions import (mongo, swapi)


class Planet(Resource):
    """ Class that contains all methods used in the API regarding the planets
    Inherits from Resource to use advantage of flask_restful power.
    """

    @staticmethod
    def transform_data(data:dict)->dict:
        return {
                "id": str(data['_id']),
                "name": data['name'],
                "climate": data['climate'],
                "terrain": data['terrain'],
                "apparitionsCount": swapi.getPlanet(data['name'])
                }
        
    @staticmethod
    def get(planet_id=None, planet_name=None)->jsonify:
        """GET HTTP Verb for the Planets

        Returns:
            jsonify -- A jsonified object from a dict holding
                        a planet info.
        """
        data = list()
        
        
        if planet_id:
            planet = mongo.db.planets.find_one({"_id": ObjectId(planet_id)})
            if planet:
                data.append(Planet.transform_data(planet))
        elif planet_name:
            planet = mongo.db.planets.find_one({"name": planet_name})
            if planet:
                data.append(Planet.transform_data(planet))
        else:
            for planet in mongo.db.planets.find():
                data.append(Planet.transform_data(planet))
        
        if len(data) == 0:
            resp = jsonify([])
            resp.status_code = 204 # No content
            return resp

        return jsonify(data)

    @staticmethod
    def post():
        data = request.get_json()

        if not data:
            return error_message(422, 'No data to insert.') # Unprocessable Entity
        else:
            if mongo.db.planets.find_one({"name": data.get('name')}):
                return error_message(409, 'This planet already exists.') # Conflict
            else:
                print(data.get('name'))
                planetApparitions = swapi.setPlanet(data.get('name'))
                
                if not planetApparitions:
                    return error_message(403, 'This planet was not found on StarWars API.') # Prohibited 
                
                inserted = mongo.db.planets.insert(data)
                inserted = mongo.db.planets.find_one({"_id": ObjectId(inserted)})

        resp = jsonify(Planet.transform_data(inserted))
        resp.status_code = 201 # Created
        return resp

    @staticmethod
    def put(planet_id:str=None)->redirect:
        data = request.get_json()
        if not data or not planet_id:
            return error_message(422, 'No planet id or data to update.') # Unprocessable Entity
        else:
            print(planet_id, data)
            updated = mongo.db.planets.update({'_id': ObjectId(planet_id)}, {'$set': data})
            updated = mongo.db.planets.find_one({"_id": ObjectId(planet_id)})
            resp = jsonify(Planet.transform_data(updated))
            resp.status_code = 200 # Updated
            return resp


    @staticmethod
    def delete(planet_id:str=None, planet_name:str=None)->redirect:
        if planet_id:
            mongo.db.planets.remove({'_id': ObjectId(planet_id)})
        elif planet_name:
            mongo.db.planets.remove({'name': planet_name})
        else:
            error_message(422, 'No planet id or planet name to delete')
        resp = jsonify(list())
        resp.status_code = 204 # Deleted
        return resp
