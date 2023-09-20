#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
import shlex
from importlib import import_module
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects ={}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict
    
    def delete(self, obj=None):
        """Removes an object from the storagee dictionary"""
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.key():
                del self.__objects[obj_key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Load storage dict from file"""
        classes = self.model_classes
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
    
    def close(self):
        """closes the storage engine"""
        self.reaload()