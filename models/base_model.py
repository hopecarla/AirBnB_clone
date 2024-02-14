#!/usr/bin/python3
"""Defines the BaseModel class."""


import uuid
from datetime import datetime


class BaseModel:
    """Base class for other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes

        If there are no keyword arguments provided, generate a new UUID for the `id`
        attribute and set the `created_at` and `updated_at` attributes to the current
        datetime then add the new instance to the storage.

        if keyword arguments are provided then convert the `created_at` and `updated_at`
        attributes from string format to datetime format and set the instances
        attributes appropriately.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items();
                if key != "__class__":
                    setattr(self, key, val)

    def __str__(self):
        """String representation of the BaseModel instance"""
        return f"[{self.__class__name}] ({self.id}) {self.__dict__}"

    __repr__ =  __str__

    def save(self):
        """Updates the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel"""
        return{
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
        }
