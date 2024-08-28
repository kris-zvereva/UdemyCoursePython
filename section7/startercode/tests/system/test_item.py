import json

from section7.startercode.models.item import ItemModel
from section7.startercode.models.user import UserModel
from section7.startercode.models.store import StoreModel
from section7.startercode.tests.base_test import BaseTest


class TestItem(BaseTest):
    def setUp(self):
        super(TestItem, self).setUp()
        with self.app as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_response = client.post('/auth',
                                            json={'username': 'test', 'password': '1234'},
                                            headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_response.data)['access_token']
                self.header = {'Authorization': 'Bearer ' + auth_token}

    def test_get_item_no_auth(self):
        with self.app as client:
            with self.app_context():
                response = client.get('/item/list')
                self.assertEqual(response.status_code, 401)  # no auth header so 401

    def test_get_item_not_found(self):
        with self.app as client:
            with self.app_context():
                response = client.get('/item/test', headers=self.header)
                print(response.data)  # Debugging step to see the actual response
                self.assertEqual(404, response.status_code)

    def test_get_item(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.get('/item/test', headers=self.header)
                print(response.data)  # Debugging step to see the actual response
                self.assertEqual(200, response.status_code)

    def test_delete_item(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.delete('/item/test')
                self.assertEqual(200, response.status_code)
                self.assertDictEqual({'message': 'Item deleted'},
                                     json.loads(response.data))

    def test_create_item(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()

                response = client.post('/item/test',
                                       json={'price': 19.94, 'store_id': 1})
                self.assertEqual(201, response.status_code)
                self.assertDictEqual({'name': 'test', 'price': 19.94}, json.loads(response.data))

    def test_create_duplicate_item(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                client.post('/item/test', json={'price': 19.94, 'store_id': 1})
                response = client.post('/item/test',
                                       json={'price': 19.94, 'store_id': 1})
                self.assertEqual(400, response.status_code)
                self.assertDictEqual({'message': "An item with name 'test' already exists."}, json.loads(response.data))

    def test_put_item(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response = client.put('/item/test',
                                      json={'price': 18.99, 'store_id': 1})
                self.assertEqual(200, response.status_code)
                self.assertEqual(ItemModel.find_by_name('test').price, 18.99)
                self.assertDictEqual({'name': 'test', 'price': 18.99},
                                     json.loads(response.data))

    def test_put_update_item(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 5.59, 1).save_to_db()
                self.assertEqual(ItemModel.find_by_name('test').price, 5.59)

                response = client.put('/item/test',
                                      json={'price': 18.99, 'store_id': 1})
                self.assertEqual(200, response.status_code)
                self.assertEqual(ItemModel.find_by_name('test').price, 18.99)

    def test_item_list(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 5.59, 1).save_to_db()

                response = client.get('/items')
                self.assertEqual(200, response.status_code)
                self.assertDictEqual({'items': [{'name': 'test', 'price': 5.59}]},
                                     json.loads(response.data))

