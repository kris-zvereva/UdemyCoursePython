from section7.startercode.models.store import StoreModel
from section7.startercode.models.item import ItemModel
from section7.startercode.tests.base_test import BaseTest


class TestStore(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'), "Found an store with name 'test' before save_to_db")

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                 "Did not find an store with name 'test' after save_to_db")

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'), "Found an store with name 'test' after delete_from_db")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')
