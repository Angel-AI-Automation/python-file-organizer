# File Organizer Automation Script (Python)

## Overview
This project is a Python automation script designed to organize files automatically by type.  
It reduces manual work, minimizes human error, and improves productivity when managing unstructured folders.

## Why This Project Matters
Manual file organization is a common but inefficient task in many workplaces.  
This project demonstrates how simple Python automation can solve a real operational problem using clean, maintainable code.

## Problem Statement
In many real-world environments, files accumulate in a single directory without structure.  
This leads to disorganization, repetitive manual tasks, increased errors, and wasted time.

## Solution
The script scans a source folder, identifies files based on their extensions, and moves them into categorized folders inside an output directory.  
This approach automates repetitive work and improves file management efficiency.

## Features
- Automatic file organization by file extension  
- Command-line interface support  
- Clear and reusable automation logic  
- Simple folder-based workflow  
- Easily extendable for future improvements  

## How to Run
```bash
py automation/organize_files.py files_input files_output
```
Make sure both folders exist before running the script.

## Use Cases

- Office and administrative environments
- Universities and academic institutions
- Freelancers managing multiple document types
- Small businesses and personal productivity workflows

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

## Code Design Notes

- The script uses clear function separation to improve readability.
- Early exits are applied to avoid unnecessary processing.
- The project is intentionally kept simple to ensure maintainability.