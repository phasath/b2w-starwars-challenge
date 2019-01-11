"""Tool to make query on SW API regarding the planets"""
from requests import get
from retrying import retry
from cachetools import cached, TTLCache

CACHE = TTLCache(maxsize=100, ttl=300)

class SWAPI:
    """Class to hold information about the planets
    apparitions count and request the Star Wars API."""
    def __init__(self):
        """Initializer of the class. The class contains
        only a dict in which keys represents the planets
        and values are the apparitions count.
        """
        self.data = {}

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=2000)
    def get_apparitions_count(planet_name: str)->[bool, int]:
        """Fuction to get the data of how many times a planet appeared on movies.
        This function makes a request on star-wars api and keeps retrying if no
        response waiting for a random interval between 1 and 2 seconds.

        Arguments:
            planet_name {str} -- planet name to be queried on star wars api

        Raises:
            ValueError -- An error recommended by the retrying package
            to make the function run again.

        Returns:
            [False or Int] -- False in case no result was found,
            meaning that this planet doesn't exist on StarWars API.
            It cannot be zero as there are many planets that has never been in movies.
            When it's an Int, it indicates how many movies that planet appeared.
        """
        data = get(url=f'https://swapi.co/api/planets/?search={planet_name}&format=json')
        if data.status_code == 200:
            data = data.json()
            if data['count'] == 0:
                return False
            return len(data['results'][0]['films'])

        raise ValueError

    def set_planet(self, planet_name: str)->bool:
        """ Setter function to put a planet on the dictionary.

        Arguments:
            planet_name {str} -- planet name

        Returns:
            Bool -- Indicates whether it could or not insert the planet.
        """
        resp = SWAPI.get_apparitions_count(planet_name)
        if resp is not False:
            self.data[planet_name] = resp
            return True

        return False

    @cached(CACHE)
    def get_planet(self, planet_name: str)->int:
        """Getter function that returns the planet.

        It's cached because we don't save on the DB information about the planet.
        This way, we'll always have the most updated information about the planet.

        If the planet doesn't exist, it'll make a request on
        StarWars API to get information about it.

        The cache holds data for 300s

        Arguments:
            planet_name {str} -- the planet name

        Returns:
            Int -- the apparitions count of this planet
        """
        if not self.data.get(planet_name, None):
            self.set_planet(planet_name)
        return self.data[planet_name]
