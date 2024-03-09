#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage
my_storage = FileStorage()
my_storage.reload()
