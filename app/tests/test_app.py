import unittest

from flask import Flask

from app.autoapp import APP
from app.api.extensions import CFG

class AppTest(unittest.TestCase):

    def test_app_is_flask_instance(self):
        with APP.app_context():
            self.assertIsInstance(APP, Flask)

    def test_environment_is_set(self): 
        with APP.app_context():
            self.assertIn(CFG.ENV,['development','production','test','stage'])
    

