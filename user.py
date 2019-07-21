###########CLASS USER#########
class User:
    """
    Class that generates new instances of users.
    """

    user_list = []

    def save_user(self):
    
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)



    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
