#!/usr/bin/python3
'''
    Application of the User class that inherits from the BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
        Definition of the User Class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
