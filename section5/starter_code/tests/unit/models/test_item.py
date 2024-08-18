from starter_code.tests.unit.unit_base_test import UnitBaseTest
from starter_code.models.item import ItemModel


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test name', 34.55, 1)
        self.assertEqual('test name', item.name,
                         'The name of the item after creation is not equal the constructor argument.')
        self.assertEqual(34.55, item.price,
                         'The price of the item after creation is not equal the constructor argument.')
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_json(self):
        item = ItemModel('test name', 34.55, 1)
        expected = {
            'name': 'test name',
            'price': 34.55,
        }

        self.assertDictEqual(item.json(), expected,
                             'The JSON export of the item is incorrect. Received {}, expected {}'.format(item.json(), expected))



