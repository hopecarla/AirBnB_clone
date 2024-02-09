#!/usr/bin/python3
'''
   The definition of the city Class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Defines the City class that inherits from the BaseModel.
    '''
    state_id = ""
    name = ""
