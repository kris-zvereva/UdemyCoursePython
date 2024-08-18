from section4.app.tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:  # initialising a context manager
            resp = c.get('/')  # calling the endpoint, resp = response

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(
                json.loads(resp.get_data()),  # converts to a dict
                {'message': 'Hello, world!'}
                )
