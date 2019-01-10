from unittest import TestCase
from pymongo import TEXT
from random import randint
from requests import get
from retrying import retry

from app.autoapp import APP
from app.api.extensions import (MONGO, CFG)

def app_context(func):
    """ Decorator function to apply app_context """
    def func_wrapper(*args, **kwargs):
        with APP.app_context():
            return func(*args, **kwargs)
        return func_wrapper

class BaseTest(TestCase):

    def setUp(self):
        MONGO.init_app(app=APP, uri=CFG.MONGODB_URI)
        
        #delete planets collection:
        MONGO.db.planets.drop()

        #recreates planets collection:
        MONGO.db.planets.create_index([('idx_planet_name', TEXT)], name='search_index',
                                  default_language='english', unique=True, background=True)


    @retry()
    def create_planet(self,planet_id: int = None)->bool:
        """ Create a random planet and insert it on the database.
        It gets a random planet from the swapi if no planet_id is passed.
        From the swapi, there are 61 planets.
        """

        if not planet_id:
            planet_id = randint(1,62) 
        
        data = get(url=f'https://swapi.co/api/planets/{planet_id}/?format=json')
        if data.status_code == 200:
            data = data.json()
            planet_data = {"name": data['name'], "terrain": data['terrain'], "climate": data["climate"]}
            planet_inserted = MONGO.db.planets.insert_one(planet_data)

            return {"id": str(planet_inserted.inserted_id),
                    "name": data['name'],
                    "terrain": data['terrain'],
                    "climate": data["climate"],
                    "apparitions_count": len(data['films'])
                    }
            
            

        raise ValueError