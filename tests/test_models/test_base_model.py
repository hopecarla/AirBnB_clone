#!/usr/bin/python3
'''
    All the base_model tests are applied here
'''


import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBase(unittest.TestCase):
    '''
        BaseModel class testing
    '''

    def setUp(self):
        '''
            Initializing an instance
        '''
        self.my_model = BaseModel()
        self.my_model.name = 

    def TearDown(self):
        '''
            Removimg instance
        '''
        del self.my_model
        
    def test_id_type(self):
        '''
            Checks that the id's type is a string
        '''
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        '''
            Checks that the ids of both instances are different
        '''
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        '''
            Checks if an attribute has been added
        '''
        self.assertEqual(

    def test_updated_created_equal(self):
        '''
            Checks if the dates are equal
        '''
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_save(self):
        '''
            Checks if the dates differ after updating the instance
        '''
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_str_overide(self):
        '''
            Checks if the right message was printed
        '''
        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        '''
            Checks the to_dict method returns type
        '''

        self.assertEqual("<class 'dict'>",
                         str(type(self.my_model.to_dict())))

    def test_to_dict_class(self):
        '''
            Checks that the __class__ key exists
        '''
        
        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        '''
            Checks the type of the value in updated_at
        '''
        self.assertEqual("<class 'str'>",
                          str(type((self.my_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        '''
            Checks the type of the value in created_at
        '''
        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        '''
            Test that an instance was created using th ekey value pair
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        '''
            Test that the new_model's updated_at 
            type is datetime
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        '''
            Test that the new model's created_at
            type is datetime
        '''
        my_model_dict = self.my_model._to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        '''
            Test that the dictionary values of the new_model and my_model
            are the same
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)

    def test_instance_diff(self):
        '''
            Test that my_model and the new_model are not the same
            instance
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertNotEqual(self.my_model, new_model)
