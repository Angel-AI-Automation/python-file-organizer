"""
Filesystem interaction module.

Handles OS-level operations such as listing and moving files.
"""

import os
import shutil
import logging


def list_files(directory: str):
    return os.listdir(directory)


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def ensure_directory(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def move_file(source: str, destination: str):
    try:
        shutil.move(source, destination)
    except PermissionError:
        logging.error(f"Permission denied while moving file: {source}")