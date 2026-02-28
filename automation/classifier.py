"""
Business logic module.

Contains pure functions responsible for file classification.
"""

def get_extension(filename: str) -> str:
    """
    Extracts the file extension from a filename.
    Returns 'no_extension' if none is found.
    """
    if "." in filename:
        return filename.split(".")[-1].lower()
    return "no_extension"