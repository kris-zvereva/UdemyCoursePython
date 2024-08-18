from unittest import TestCase
from section4.app.app import app


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True  # testing mode is on
        self.app = app.test_client
