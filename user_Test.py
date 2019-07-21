import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the Users class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    #########First test #########

    def setUp(self):
         #setup method to run before each test cases.

        self.new_user = User ("vinceouma@gmail.com", "vincentouma", "vinceobindi1005")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.email,"vinceouma@gmail.com")
        self.assertEqual(self.new_user.username,"vincentouma")
        self.assertEqual(self.new_user.password,"vinceobindi1005")


if __name__ == '__main__':
    unittest.main()

