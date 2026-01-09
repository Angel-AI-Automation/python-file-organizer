# Automation Scripts

## Overview
This directory contains Python automation scripts designed to solve practical file management problems.
The scripts focus on clarity, reusability, and real-world command-line usage.

They are intentionally simple, well-structured, and easy to extend, making them suitable for learning,
personal productivity, and small automation tasks.

---

## Scripts Included

- **organize_files.py**  
  Automatically organizes files from an input directory into an output directory.
  Files are processed based on their extensions and moved into categorized folders.

---

## How It Works

1. Reads all files from the specified input directory
2. Validates that both input and output directories exist
3. Skips execution if the source directory is empty
4. Identifies file types by extension
5. Moves files into categorized folders inside the output directory
6. Prevents crashes by handling common edge cases

---

## Usage

Run the script from the project root using the command line:

```bash
py automation/organize_files.py files_input files_output
```
## Optional: Safe Execution (Dry Run)

The script supports a dry-run mode that previews file operations without making changes.
This is useful for testing behavior before running it in production environments.

```bash
py automation/organize_files.py files_input files_output --dry-run
```
## Technologies Used

- Python
- Standard libraries (os, sys, shutil)
- Command-line execution
- Git & GitHub

## Future Improvements

- Logging system for file operations
- Support for additional file formats
- Improved CLI arguments and flags
- Optional user interface
