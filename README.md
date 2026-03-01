# File Organizer Automation Tool (Python)

## Overview

This project is a modular Python automation tool designed to organize files automatically by type. 
It reduces manual work, minimizes human error, and improves productivity when managing unstructured folders.

The project was refactored from a monolithic script into a modular architecture to improve maintainability, scalability, and testability.

---

## Problem Statement

In many real-world environments, files accumulate in a single directory without structure. 
This leads to disorganization, repetitive manual tasks, increased errors, and wasted time.

---

## Solution

The application scans a source folder, identifies files based on their extensions, and moves them into categorized folders inside an output directory.

The logic responsible for classification is separated from filesystem operations to ensure clean architecture and easier testing.

---

## Architecture Design

The project follows a modular structure:

- **Business Logic Layer** (`classifier.py`) 
Handles file extension extraction and classification logic.

- **Filesystem Layer** (`filesystem.py`) 
Encapsulates OS-level operations such as listing files, creating directories, and moving files.

- **Orchestrator Layer** (`organizer.py`) 
Coordinates business logic and filesystem interactions.

- **CLI Entry Point** (`main.py`) 
Handles argument parsing, validation, and execution flow.

This separation improves:

- Maintainability
- Testability
- Low coupling
- Clear responsibility boundaries

---

## Features

- Automatic file organization by file extension
- Modular architecture with separated concerns
- Command-line interface support
- Logging for execution tracking
- Easily extendable structure for future improvements

---

## How to Run

```bash
python main.py files_input files_output
```
 
## Use Cases

- Office and administrative environments
- Universities and academic institutions
- Freelancers managing multiple document types
- Small businesses and personal productivity workflows

---
## Technologies Used

- Python
- Standard Library (os, shutil, sys, logging)
- Modular package structure
- Command-line execution
- Git & GitHub for version control

---
## Future Improvements

- Unit testing with pytest
- Dry-run mode (simulate file moves)
- Improved CLI argument parsing (argparse)
- Structured logging improvements
- Configuration-based file categorization

 
## Code Design Principles

- Separation of concerns
- Encapsulation of system interaction
- Isolated and testable business logic
- Clear orchestration layer
- Maintainable and scalable structure

This project demonstrates practical automation skills with clean architectural thinking suitable for junior technical roles.



