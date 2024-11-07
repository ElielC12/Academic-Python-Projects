"""
Program: LAB A Redact
Author: Eliel Cortes
Professor: Prof. Ordonez
Date: 2024-11-07
"""

import os
import re

def get_file_path():
    """Prompts the user for a filename and returns the full path."""
    file_name = input("Path to file: ")
    return os.path.join(os.getcwd(), file_name)

def get_redact_word():
    """Prompts the user for the word to redact."""
    return input("Word to redact: ")

def redact_content(file_path, redact_word):
    """Reads the file, replaces occurrences of the redact_word with X's, and returns the new content."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Create a string with the same number of X's as the word length
        redact_replace = 'X' * len(redact_word)
        
        # Use regular expressions for case-insensitive replacement
        # \b ensures the word is replaced as a whole word, not part of another word
        pattern = re.compile(re.escape(redact_word), re.IGNORECASE)
        redacted_content = pattern.sub(redact_replace, content)
        
        return redacted_content, redact_replace
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None, None

def save_redacted_content(file_path, redacted_content):
    """Saves the redacted content into a new file with 'REDACTED-' prepended to the filename."""
    base_name = os.path.basename(file_path)
    new_file_path = os.path.join(os.path.dirname(file_path), f"REDACTED-{base_name}")
    
    with open(new_file_path, 'w') as new_file:
        new_file.write(redacted_content)
    
    return new_file_path

def main():
    # Get the file path and the word to redact
    file_path = get_file_path()
    redact_word = get_redact_word()

    # Get the redacted content and the word replacement
    redacted_content, redact_replace = redact_content(file_path, redact_word)
    
    if redacted_content is not None:
        # Save the redacted content to a new file
        new_file_path = save_redacted_content(file_path, redacted_content)

        base_filename = os.path.basename(file_path)
        
        # Let the user know what the word was replaced with
        print(f"REDACTED-{base_filename} shows \"{'X' * len(redact_word)}\" instead of every occurrence of \"{redact_word}\".")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
