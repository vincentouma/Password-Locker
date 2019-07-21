###########CLASS USER#########
class User:
    '''
    Class that generates new instances of user
    '''
    user_list = [] #list of users to be stored here

    def save_user(self):
        '''
        saving user credentials into user_list for login
        '''
        User.user_list.append(self)