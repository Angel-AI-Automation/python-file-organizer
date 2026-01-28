"""
File Organizer Script

Organizes files from a source folder into an output folder based on file extensions.
Designed to be simple, reusable, and suitable for small office or administrative
automation tasks.
"""

import os
import sys
import shutil
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_folders(source_folder, output_folder):
    if not os.path.exists(source_folder):
        logging.error(f"Source folder does not exist: {source_folder}")
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


def organize_files(source_folder, output_folder):
    logging.info("Starting file organization process")

    if not os.listdir(source_folder):
        logging.warning("Source folder is empty. No files to organize.")
        return False

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            if "." in filename:
                extension = filename.split(".")[-1].lower()
            else:
                extension = "no_extension"

            extension_folder = os.path.join(output_folder, extension)

            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            try:
                shutil.move(file_path, os.path.join(extension_folder, filename))
            except PermissionError:
                logging.error(f"Permission denied while moving file: {filename}")

    logging.info("File organization process completed successfully")
    return True


def main():
    logging.info("Program started")

    if len(sys.argv) != 3:
        logging.error("Usage: py organize_files.py <source_folder> <output_folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    output_folder = sys.argv[2]

    validate_folders(source_folder, output_folder)

    files_processed = organize_files(source_folder, output_folder)

    if files_processed:
        logging.info(
            f"Files from '{source_folder}' were successfully organized into '{output_folder}'."
        )

    logging.info("Program finished")


if __name__ == "__main__":
    main()
