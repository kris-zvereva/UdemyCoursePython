from section7.startercode.models.user import UserModel
from section7.startercode.tests.base_test import BaseTest


class TestUser(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'password')

        self.assertEqual(user.username, 'test',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'password',
                         "The password of the user after creation does not equal the constructor argument.")
