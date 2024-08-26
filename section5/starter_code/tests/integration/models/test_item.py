from section5.starter_code.models.item import ItemModel
from section5.starter_code.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99, 1)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              'found an item with a name {}, but expected not to'.format(item.name))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 'did not find an item with a name {}, but expected to'.format(item.name))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'),
                              'found an item with a name {}, but expected not to'.format(item.name))
