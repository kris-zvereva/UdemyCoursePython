from unittest import TestCase
from section4.app.app import app
import json


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:  # initialising a context manager
            resp = c.get('/')  # calling the endpoint, resp = response

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(
                json.loads(resp.get_data()),  # converts to a dict
                {'message': 'Hello, world!'}
                                        )
