import unittest
from application.models import Users

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = Users(password = 'mayai')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_hash is not None)
    
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('mayai'))