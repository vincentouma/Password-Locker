class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    cred_list = []

#########Assign propety to credentil list#########
    def __init__(self, account , email , passlock):
    
        self.account = account
        self.email = email
        self.passlock = passlock