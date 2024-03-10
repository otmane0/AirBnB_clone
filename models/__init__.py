#!/usr/bin/python3
"""module from dir"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()