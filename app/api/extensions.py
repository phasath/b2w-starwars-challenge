"""Create all the extensions used on the app"""

from decouple import config
from app.api.settings import config_to_class

ENV = config('ENV', default='production')

CFG = config_to_class(ENV)