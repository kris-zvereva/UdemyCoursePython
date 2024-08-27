from section5.starter_code.models.item import ItemModel
from section5.starter_code.models.store import StoreModel
from section5.starter_code.tests.integration.integration_base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('Test')

        self.assertEqual(store.items.all(), [],
                         'the store items is not empty but expected to')

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'))
            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('test'))
            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('test'))

    def test_store_relationships(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test item', 21.22, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test item')

    def test_store_json(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test item', 21.22, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'test',
                'items': [{'name': 'test item',
                           'price': 21.22}],
            }

            self.assertDictEqual(store.json(), expected)


