#!/usr/bin/python3
"""Make unique Filestorage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()