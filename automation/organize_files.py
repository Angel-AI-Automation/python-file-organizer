"""
File Organizer Script

Organizes files from a source folder into an output folder based on file extensions.
Designed to be simple, reusable, and suitable for small office or administrative
automation tasks.
"""

import os
import sys
import shutil


def validate_folders(source_folder, output_folder):
    if not os.path.exists(source_folder):
        print(f"Error: Source folder does not exist -> {source_folder}")
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


def organize_files(source_folder, output_folder):
    if not os.listdir(source_folder):
        # Early exit to avoid unnecessary processing when the folder is empty
        print("Source folder is empty. No files to organize.")
        return

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            extension = filename.split(".")[-1].lower()
            extension_folder = os.path.join(output_folder, extension)

            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            shutil.move(file_path, os.path.join(extension_folder, filename))


def main():
    if len(sys.argv) != 3:
        print("Usage: py organize_files.py <source_folder> <output_folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    output_folder = sys.argv[2]

    validate_folders(source_folder, output_folder)
    organize_files(source_folder, output_folder)

    print(
        f"Files from '{source_folder}' were successfully organized into '{output_folder}'."
    )


if __name__ == "__main__":
    main()