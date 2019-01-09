"""Tool to make query on SW API regarding the planets"""
from requests import get
from retrying import retry
from cachetools import cached, TTLCache 

cache = TTLCache(maxsize=100, ttl=300)

class SWAPI:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=2000) # wait between 1 and 2 seconds before trying again
    def getApparitionsCount(planet_name:str):
        data = get(url=f'https://swapi.co/api/planets/?search={planet_name}&format=json')
        if data.status_code == 200: 
            data = data.json()
            if data['count'] == 0:
                return False
            else:
                return len(data['results'][0]['films'])
        else:
            raise ValueError
            

    def setPlanet(self, planet_name:str):
        resp = SWAPI.getApparitionsCount(planet_name)
        if resp is not False:
            self.data[planet_name] = resp
            return True
        else:
            return False
    
    @cached(cache)
    def getPlanet(self, planet_name:str):
        if not self.data.get(planet_name, None):
            self.setPlanet(planet_name)            
        return self.data[planet_name]