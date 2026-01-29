# Automation Scripts

## Overview
This directory contains Python automation scripts focused on solving practical file management problems.  
The scripts prioritize clarity, reusability, and real-world command-line usage.

They are intentionally simple and well-structured, making them suitable for learning, personal productivity, and small automation tasks.

## Scripts Included

### organize_files.py
Automatically organizes files from an input directory into an output directory.  
Files are categorized based on their extensions and moved into structured folders.

## How It Works
1. Reads all files from the specified input directory  
2. Validates that both input and output directories exist  
3. Skips execution if the source directory is empty  
4. Identifies file types by extension  
5. Moves files into categorized folders inside the output directory  
6. Handles basic edge cases such as empty source folders and invalid directory paths
   to prevent unexpected crashes during execution.  

## Usage
Run the script from the project root using the command line:

```bash
py automation/organize_files.py files_input files_output
```

## Optional: Safe Execution (Planned Feature)

A dry-run mode is planned to allow users to preview file operations
without making changes to the file system. This feature is not yet implemented
and is listed as a future improvement.

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