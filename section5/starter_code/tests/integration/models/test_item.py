from starter_code.models.item import ItemModel
from starter_code.models.store import StoreModel
from starter_code.tests.integration.integration_base_test import BaseTest


class TestItem(BaseTest):
    def test_create_item(self):
        with self.app_context():  # running the app
            store = StoreModel('test')
            store.save_to_db()
            item = ItemModel('test name', 19.90, 1)

            self.assertIsNone(ItemModel.find_by_name('test name'),
                              f'Found an item with name {item.name}, but expected not to.')  # checking it doesnt exist
            item.save_to_db()  # saving
            self.assertIsNotNone(ItemModel.find_by_name('test name'),
                                 f'Item with name {item.name} is not saved to the db.')  # checking it exists

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test name'),
                              f'Item with name {item.name} found, but expected not to.')

    def test_store_relationships(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test name', 34.55, 1)
            # all stores have id=1 because in base test we delete everything from db

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')

