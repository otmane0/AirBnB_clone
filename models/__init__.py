#!/usr/bin/python3
"""Initialize the models package by creating a unique FileStorage instance."""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload() # Load existing data from the JSON file (if it exists)

    # https://www.youtube.com/@Nightlights2/videos
