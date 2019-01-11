""" Module to test the Planets resource """
from bson.objectid import ObjectId

from app.tests import BaseTest
from app.autoapp import APP

from app.api.resources.planets import Planet


class PlanetsTest(BaseTest):
    """ Tests for all the HTTP Verbs from Planets class """

    def test_transform_data(self):
        """ Test if the function is correctly casting the data
        And is getting the apparitions_count from the SWAPI
        """

        data = {"_id": ObjectId(), "name":"Alderaan", "climate":"temperate", "terrain":"grasslands, mountains"}

        transformed_data = Planet.transform_data(data)

        data["id"] = str(data['_id'])
        del data['_id']

        for key in data.keys():
            self.assertEqual(data[key], transformed_data[key])

    def test_get_all_planets(self):
        """Test if planets will return as expected.
        """

        BaseTest.create_planet(planet_id=1)
        BaseTest.create_planet(planet_id=2)

        client = APP.test_client()
        response = client.get('/api/planets').json

        expected = [{"name": "Tatooine", "climate": "arid",
                     "terrain": "desert", "apparitions_count": 5},
                    {"name": "Alderaan", "climate": "temperate",
                     "terrain":"grasslands, mountains", "apparitions_count": 2}]

        keys = expected[0].keys()

        for idx, planet in enumerate(response):
            for key in keys:
                self.assertEqual(planet[key], expected[idx][key],
                                 f'{planet[key]} is not equals to {expected[idx][key]}')

    def test_get_one_planet_by_id(self):
        """Tests if searching for planet id will return as expected
        """

        planet_data = BaseTest.create_planet()
        client = APP.test_client()
        response = client.get(f"/api/planets/{planet_data['id']}").json

        for key in planet_data:
            self.assertEqual(response[0][key], planet_data[key])

        response = client.get(f"/api/planets/id/{planet_data['id']}").json

        for key in planet_data:
            self.assertEqual(response[0][key], planet_data[key])

    def test_get_one_planet_by_name(self):
        """Tests if searching for planet name will return as expected
        """

        planet_data = BaseTest.create_planet()

        client = APP.test_client()
        response = client.get(f"/api/planets/name/{planet_data['name']}").json

        for key in planet_data:
            self.assertEqual(response[0][key], planet_data[key])

    def test_get_with_no_planet_returns_204(self):
        """Test if having no planets it will return an 204 code as expected.
        """

        client = APP.test_client()
        response = client.get('/api/planets')
        
        self.assertEqual(204, response.status_code)

    def test_if_post_inserts_a_planet(self):
        """Test if it will insert a planet correctly
        """

        planet_data = {"name":"Alderaan", "climate":"temperate", "terrain":"grasslands, mountains"}
        client = APP.test_client()

        response = client.post('/api/planets', json=planet_data)
        self.assertEqual(201, response.status_code)

        r_data = response.json
        for key in planet_data:
            self.assertEqual(r_data[key], planet_data[key])

    def test_if_post_inserts_a_planet_if_no_data_sent(self):
        """Test if it will insert a planet correctly
        """

        planet_data = {}
        client = APP.test_client()

        response = client.post('/api/planets', json=planet_data)
        self.assertEqual(422, response.status_code)

    def test_post_do_not_inserts_a_planet_if_duplicated(self):
        """Test if it will insert a planet that was already inserted
        """

        planet_data = {"name":"Alderaan", "climate":"temperate", "terrain":"grasslands, mountains"}
        client = APP.test_client()

        response1 = client.post('/api/planets', json=planet_data)
        response2 = client.post('/api/planets', json=planet_data)

        self.assertEqual(201, response1.status_code)
        self.assertEqual(409, response2.status_code)

    def test_if_post_inserts_a_planet_name_does_not_exist_on_swapi(self):
        """Test if it will not insert a planet if the name doesn't exist on swapi
        """

        planet_data = {"name":"Han Solo", "climate":"courageous", "terrain":"Millennium Falcon"}
        client = APP.test_client()

        response = client.post('/api/planets', json=planet_data)
        self.assertEqual(403, response.status_code)

    def test_if_put_updates_data_from_planet(self):
        """Test if it will update the data from a planet
        """
        planet_data = BaseTest.create_planet()

        planet_data_update = {"name":"Alderaan", "climate":"temperate",
                              "terrain":"grasslands, mountains"}

        client = APP.test_client()

        response = client.put(f"/api/planets/{planet_data['id']}", json=planet_data_update)
        self.assertEqual(200, response.status_code)

        r_data = response.json
        for key in planet_data_update:
            self.assertEqual(r_data[key], planet_data_update[key])

    def test_if_put_updates_fails_if_no_planet_id(self):
        """If there's no planet_id, then, put will not understand this
        requisition, so it must returns a 404
        """
        planet_data = BaseTest.create_planet()

        planet_data_update = {"name":"Alderaan", "climate":"temperate",
                              "terrain":"grasslands, mountains"}

        client = APP.test_client()

        response = client.put(f"/api/planets/", json=planet_data_update)
        self.assertEqual(404, response.status_code)

    def test_if_put_updates_fails_if_data(self):
        """Test if it will fails if no planet_id
        """
        planet_data = BaseTest.create_planet()

        planet_data_update = {}

        client = APP.test_client()

        response = client.put(f"/api/planets/{planet_data['id']}", json=planet_data_update)
        self.assertEqual(422, response.status_code)

    def test_if_put_updates_fails_if_wrong_planet_id(self):
        """Test if it will fails if no planet_id
        """
        planet_data = BaseTest.create_planet()

        planet_data_update = {"name":"Alderaan", "climate":"temperate",
                              "terrain":"grasslands, mountains"}

        dif_id = ObjectId()

        if planet_data['id'] == str(dif_id):
            dif_id = ObjectId()

        client = APP.test_client()

        response = client.put(f"/api/planets/{ObjectId()}", json=planet_data_update)
        self.assertEqual(204, response.status_code)

    def test_if_deletes_removes_planets_by_planet_id(self):
        """Test if it will remove a planet using planet_id
        """
        planet_data = BaseTest.create_planet()

        client = APP.test_client()

        response = client.delete(f"/api/planets/{planet_data['id']}")
        self.assertEqual(204, response.status_code)

    def test_if_deletes_removes_planets_by_planet_name(self):
        """Test if it will remove a planet using planet_name
        """
        planet_data = BaseTest.create_planet()

        client = APP.test_client()

        response = client.delete(f"/api/planets/delete/{planet_data['name']}")
        self.assertEqual(204, response.status_code)

    def test_if_do_not_deletes_if_no_planet_name(self):
        """Test if it will remove a planet using planet_name
        """
        planet_data = BaseTest.create_planet()

        client = APP.test_client()

        response = client.delete(f"/api/planets/delete/")
        self.assertEqual(422, response.status_code)
