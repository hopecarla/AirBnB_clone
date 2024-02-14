#!/usr/bin/python3

'''
    All the User Model's test are appplied here
'''

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
    '''
        Place class Testing
    '''

    def setUp(self):
        '''
            Creates instance for Place
        '''
        self.new_place = Place()
    
    def TearDown(self):
        pass

    def test_Place_inheritance(self):
        '''
            Tests that Place class inherited from BaseModel
        '''

        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        '''
            Checks the attribute's existence
        '''
        self.assertTrue("city_id" in self.new_place.__dir__())
        self.assertTrue("user_id" in self.new_place.__dir__())
        self.assertTrue("description" in self.new_place.__dir__())
        self.assertTrue("name" in self.new_place.__dir__())
        self.assertTrue("number_rooms" in self.new_place.__dir__())
        self.assertTrue("max_guest" in self.new_place.__dir__())
        self.assertTrue("price_by_night" in self.new_place.__dir__())
        self.assertTrue("latitude" in self.new_place.__dir__())
        self.assertTrue("longitude" in self.new_place.__dir__())
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    def test_type_amenity(self):
        '''
            Latitude type test
        '''
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)
    
    def test_type_longitude(self):
        '''
            Longitude type Test
        '''
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        '''
            Latitude type Test
        '''
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_price_by_night(self):
        '''
            Price by night type test
        '''
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        '''
            Max guest type test
        '''
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        '''
            Number of bathrooms type test
        '''
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        '''
            Number of rooms type test
        '''
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        '''
            Description type Test
        '''
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    def test_type_name(self):
        '''
            Name type test
        '''
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        '''
            User id type test
        '''
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_city(self):
        '''
            City_id test
        '''
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
