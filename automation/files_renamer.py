"""
Sample File Generator

Utility script used to generate sample text files for testing
file organization and automation workflows.
"""

sample_files = ["report.txt", "data.txt", "summary.txt"]

for filename in sample_files:
    with open(filename, "w") as file:
        file.write("This file was generated automatically for testing purposes.\n")

print("Sample test files created successfully.")