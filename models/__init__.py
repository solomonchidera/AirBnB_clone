#!/usr/bin/python3
"""module models"""

from models.engine.file_storage import FileStorage

classes = {'BaseModel': 'BaseModel', 'User': 'User'}
storage = FileStorage()
storage.reload()
