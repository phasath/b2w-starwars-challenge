""" Test module to check whether APP has been correctly initialized"""

import unittest

from flask import Flask

from app.autoapp import APP
from app.api.extensions import CFG

class AppTest(unittest.TestCase):
    """ Test Class for the APP """

    def test_app_is_flask_instance(self):
        """ Test to check whether app is a Flask instance.
            This means flask started properly
        """
        with APP.app_context():
            self.assertIsInstance(APP, Flask)

    def test_environment_is_set(self):
        """ Test to check whether the environment has been sucessfully set
        and is one of the expected ones.
        """
        with APP.app_context():
            self.assertIn(CFG.ENV, ['development', 'production', 'test', 'stage'])
