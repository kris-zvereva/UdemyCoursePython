from section7.startercode.models.user import UserModel
from section7.startercode.tests.base_test import BaseTest


class TestUser(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'password')

            self.assertIsNone(UserModel.find_by_username('test'), "Found an user with name 'test' before save_to_db")
            self.assertIsNone(UserModel.find_by_id(1), "Found an user with id '1' before save_to_db")

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'),
                                 "Did not find an user with name 'test' after save_to_db")
            self.assertIsNotNone(UserModel.find_by_id(1), "Did not find an user with id '1' after save_to_db")
