#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """a test class TestFileStorage that
    inherits from unittest.TestCase"""
    def setUp(self):
        """called before each test method"""
        self.file_storage = FileStorage()

    def tearDown(self):
        """called after each test method"""
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all(self):
        """test the all function in the class"""
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """testing adding new objects to a class"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.assertIn("BaseModel." + obj.id, self.file_storage.all())

    def test_save_and_reload(self):
        """Testing the 2 most important methods
        reload and save"""
        # Set maxDiff to None before making assertions
        self.maxDiff = None
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage.reload()
        self.assertEqual(new_file_storage.all(), self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
