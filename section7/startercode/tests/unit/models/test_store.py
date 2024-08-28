from section7.startercode.models.store import StoreModel
from section7.startercode.tests.unit.unit_base_test import UnitBaseTest


class TestStore(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         "The name of the store after creation does not equal the constructor argument.")
        self.assertListEqual(store.items.all(), [],
                             "The store's items length was not 0 even though no items were added.")

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertEqual(
            store.json(),
            expected,
            "The JSON export of the store is incorrect. Received {}, expected {}.".format(store.json(), expected))
