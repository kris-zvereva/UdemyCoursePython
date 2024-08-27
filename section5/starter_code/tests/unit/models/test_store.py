from section5.starter_code.models.store import StoreModel
from section5.starter_code.tests.unit.unit_base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('Test Store')

        self.assertEqual(store.name, 'Test Store',
                         'The name of the store after creation is not equal to the constructor argument.')
