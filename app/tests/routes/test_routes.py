""" Module for test the endpoints
"""
from unittest import (TestCase, mock)

from app.autoapp import APP

from app.api.utils.swapi_querier import SWAPI

def mocked_requests_get(*args, **kwargs):
    """This method will be used by the mock to replace requests.get
    """
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://swapi.co/api/planets/?search=Tatooine&format=json':
        return MockResponse({}, 500)

    return MockResponse(None, 404)

class EndpointsResponseStatusCodeTest(TestCase):
    """ Class to test whether the responde status code of endpoints are the desired
    """
    def setUp(self)->None:
        super(EndpointsResponseStatusCodeTest, self).setUp()
        APP.testing = True
        self.get_endpoints = (
            '/',
        )


    def tearDown(self)->None:
        super(EndpointsResponseStatusCodeTest, self).tearDown()
        APP.testing = False


    def test_root_endpoints_should_return_status_code_200(self)->None:
        """ Function that tests root endpoints of HTTP Verb GET and whether they return 200
        """
        client = APP.test_client()
        for endpoint in self.get_endpoints:
            response = client.get(endpoint)
            self.assertEqual(200, response.status_code,
                             f'Endpoint {endpoint} returned status {response.status_code}')

    def test_wrong_endpoint_should_return_status_code_404(self)->None:
        """Function that tests if a non-existent endpoint will return 404 based on our
        404 app handler
        """
        client = APP.test_client()
        response = client.get('non-existent-endpoint')
        err_msg = response.json
        self.assertEqual(404, response.status_code,
                         f'Endpoint non-existent-endpoint returned status {response.status_code}')
        self.assertEqual(err_msg['err']['msg'],
                         'This route is currently not supported.\
                             Please refer API documentation.')

    @mock.patch('app.api.utils.swapi_querier.requests.get', side_effect=mocked_requests_get)
    def test_if_get_apparitions_count_raises_value_error_when_request_is_not_200(self, mock_get):
        """Test if there will raise the value error if 
        status code is not 200
        """

        swapi = SWAPI()
        response = swapi.get_apparitions_count('Tatooine')
        self.assertRaises(ValueError)


