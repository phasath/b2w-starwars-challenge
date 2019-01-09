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
        self.get_endpoints = (
            '/',
        )


    def tearDown(self)->None:
        super(EndpointsResponseStatusCodeTest, self).tearDown()
        APP.testing = False


    def test_all_get_endpoints_should_return_status_code_200(self)->None:
        """ Function that tests all endpoints of HTTP Verb GET and whether they return 200
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
