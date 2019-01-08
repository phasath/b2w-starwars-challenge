""" Module for test the endpoints
"""

from unittest import TestCase

from app.autoapp import APP

class EndpointsResponseStatusCodeTest(TestCase):
    """ Class to test whether the responde status code of endpoints are the desired
    """
    def setUp(self)->None:
        super(EndpointsResponseStatusCodeTest, self).setUp()
        APP.testing = True
        self.GET_endpoints = (
            '/',
        )

    def tearDown(self):
        super(EndpointsResponseStatusCodeTest, self).tearDown()
        APP.testing = False


    def test_all_get_endpoints_should_return_status_code_200(self)->None:
        """ Function that tests all endpoints of HTTP Verb GET and whether they return 200
        """
        client = APP.test_client()
        for endpoint in self.GET_endpoints:
            response = client.get(endpoint)
            self.assertEqual(200, response.status_code, 'Endpoint {} returned status {}'.format(endpoint, response.status_code))