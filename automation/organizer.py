"""
Orchestrator module.

Coordinates business logic and filesystem operations.
"""

import os
import logging
from .classifier import get_extension
from .filesystem import (
    list_files,
    is_file,
    ensure_directory,
    move_file,
)


def organize_files(source_folder: str, output_folder: str) -> bool:
    logging.info("Starting file organization process")

    files = list_files(source_folder)

    if not files:
        logging.warning("Source folder is empty. No files to organize.")
        return False

    for filename in files:
        file_path = os.path.join(source_folder, filename)

        if is_file(file_path):
            extension = get_extension(filename)
            extension_folder = os.path.join(output_folder, extension)

            ensure_directory(extension_folder)

            destination = os.path.join(extension_folder, filename)
            move_file(file_path, destination)

    logging.info("File organization process completed successfully")
    return True