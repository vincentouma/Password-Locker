import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_cred = Credentials("GitHub", "vinceoumah@gmail.com", "vinceobindi1005")
    def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.cred_list = []

        #######check initialization##########

    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "GitHub")
        self.assertEqual(self.new_cred.email, "vinceoumah@gmail.com")
        self.assertEqual(self.new_cred.passlock, "vinceobindi1005")

        ############7th test############

    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)