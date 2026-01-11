"""
Simple file generator for testing file organization scripts.
Creates sample text files with basic content.
"""

files = ["report.txt", "data.txt", "summary.txt"]

for file in files:
    with open(file, "w") as f:
        f.write("This file was generated automatically.\n")

print("Sample files created successfully.")