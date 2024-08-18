from unittest import TestCase
from section5.starter_code.models.item import ItemModel
from section5.starter_code.models.store import StoreModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('Test Name', 19.50, 1)
        self.assertEqual(item.name, 'Test Name',
                         'The name of the item after creation does not equal the constructor argument')
        self.assertEqual(item.price, 19.50,
                         'The name of the item after creation does not equal the constructor argument')
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('Test Name', 19.51, 1)
        expected = {
            'name': 'Test Name',
            'price': 19.51,
        }

        self.assertEqual(item.json(), expected,
                         'The json export of the item is incorrect. Received {}, expected {}'.format(item.json(), expected))
