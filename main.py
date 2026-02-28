"""
CLI entry point.
"""

import sys
import logging
import os
from automation.organizer import organize_files


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def validate_folders(source_folder: str, output_folder: str):
    if not os.path.exists(source_folder):
        logging.error(f"Source folder does not exist: {source_folder}")
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


def main():
    if len(sys.argv) != 3:
        logging.error("Usage: python main.py <source_folder> <output_folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    output_folder = sys.argv[2]

    validate_folders(source_folder, output_folder)
    organize_files(source_folder, output_folder)


if __name__ == "__main__":
    main()