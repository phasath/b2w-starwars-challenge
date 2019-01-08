from unittest import TestCase
from mock import MagicMock, patch

from app.autoapp import APP

class EndpointsResponseStatusCodeTest(TestCase):

    def setUp(self):
        super(EndpointsResponseStatusCodeTest, self).setUp()
        APP.testing = True
        self.GET_endpoints = (
            '/',
        )

    def tearDown(self):
        super(EndpointsResponseStatusCodeTest, self).tearDown()
        APP.testing = False

    def test_all_endpoints_should_return_status_code_200(self):
        client = APP.test_client()
        for endpoint in self.GET_endpoints:
            response = client.get(endpoint)
            self.assertEqual(200, response.status_code, 'Endpoint {} returned status {}'.format(endpoint, response.status_code))