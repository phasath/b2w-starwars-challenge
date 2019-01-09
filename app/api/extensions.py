"""Create all the extensions used on the app"""

from decouple import config
from flask_pymongo import PyMongo

from app.api.settings import config_to_class
from app.api.utils.swapi_querier import SWAPI as STAR_WARS_API

ENV = config('ENV', default='production')

CFG = config_to_class(ENV)

MONGO = PyMongo()
SWAPI = STAR_WARS_API()
