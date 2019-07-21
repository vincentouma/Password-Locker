import unittest # Importing the unittest module
from user import User # Importing the contact class
class TestUser(unittest.TestCase): 

    
    
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user = User("vincentouma", "vinceobindi1005") #new User created
    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []

    def test__init(self):
        '''
        check if class is initialiazing as expected
        '''
        self.assertEqual(self.new_user.username, "vincentouma")
        self.assertEqual(self.new_user.password, "vinceobindi1005")
    def test_save_user(self):
        '''
        check whether the user information can be saved 
        in the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
if __name__ == '__main__':
  unittest.main()

