#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
import random

#user 
####crate account####
def create_useraccount(username, password):
    '''
    method creates a user account
    '''
    new_user = User(username, password)
    return new_user

    ######save user#####
def save_user(user):
    '''
    method save user  account
    '''
    user.save_user()


    ######search user########

def find_user(username):
    '''
    method for find user using username
    '''
    return User.find_user(username)

