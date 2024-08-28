import json

from section7.startercode.models.item import ItemModel
from section7.startercode.models.store import StoreModel
from section7.startercode.tests.base_test import BaseTest


class TestStore(BaseTest):
    def test_create_store(self):
        with self.app as client:
            with self.app_context():
                response = client.post('/store/test')

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'name': 'test', 'items': []},
                                     json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app as client:
            with self.app_context():
                client.post('/store/test')
                response = client.post('/store/test')

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': "A store with name 'test' already exists."},
                                     json.loads(response.data))

    def test_delete_store(self):
        with self.app as client:
            with self.app_context():
                client.post('/store/test')
                response = client.delete('/store/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'},
                                     json.loads(response.data))

    def test_find_store(self):
        with self.app as client:
            with self.app_context():
                client.post('/store/test')
                response = client.get('/store/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'items': [], 'name': 'test'},
                                     json.loads(response.data))

    def test_store_not_found(self):
        with self.app as client:
            with self.app_context():
                response = client.get('/store/test')
                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(response.data))

    def test_store_found_with_items(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()

                response = client.get('/store/test')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'items': [{'name': 'test', 'price': 19.99}], 'name': 'test'},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()

                response = client.get('/stores')
                self.assertDictEqual({'stores': [{'name': 'test', 'items': []}]},
                                     json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()

                response = client.get('/stores')
                self.assertDictEqual({'stores': [{'name': 'test', 'items': [{'name': 'test', 'price': 19.99}]}]},
                                     json.loads(response.data))
