"""
payload.py

Provides a utility function for reading payload files as strings.
"""


def read_payload(file_path: str) -> str:
    """
    Read and return the contents of a text file as a stripped string.

    This function opens the file at the specified path, reads its entire content,
    strips leading and trailing whitespace (including newlines), and returns the result.

    Args:
        file_path (str): Path to the payload file to be read.

    Returns:
        str: The stripped contents of the file as a single string.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()
