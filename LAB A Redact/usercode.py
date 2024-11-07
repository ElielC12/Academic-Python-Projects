import os
import re

def get_file_path():
    """
    Prompts the user for a filename and returns the full path.
    >>> os.path.basename(get_file_path())  # assuming the input is 'psalm.txt'
    'psalm.txt'
    """
    file_name = input("Path to file: ")
    return os.path.join(os.getcwd(), file_name)

def get_redact_word():
    """
    Prompts the user for the word to redact.
    >>> get_redact_word()  # assuming the input is 'love'
    'love'
    """
    return input("Word to redact: ")

def redact_content(file_path, redact_word):
    """
    Reads the file, replaces occurrences of the redact_word with X's, and returns the new content.
    >>> redact_content('psalm.txt', 'love')  # assuming 'psalm.txt' contains 'I love you.'
    ('I XXXX you.', 'XXXX')
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Create a string with the same number of X's as the word length
        redact_replace = 'X' * len(redact_word)
        
        # Use regular expressions for case-insensitive replacement
        pattern = re.compile(re.escape(redact_word), re.IGNORECASE)
        redacted_content = pattern.sub(redact_replace, content)
        
        return redacted_content, redact_replace
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None, None

def save_redacted_content(file_path, redacted_content):
    """
    Saves the redacted content into a new file with 'REDACTED-' prepended to the filename.
    >>> save_redacted_content('psalm.txt', 'I XXXX you.')  # This will create 'REDACTED-psalm.txt'
    'REDACTED-psalm.txt'
    """
    base_name = os.path.basename(file_path)
    new_file_path = os.path.join(os.path.dirname(file_path), f"REDACTED-{base_name}")
    
    with open(new_file_path, 'w') as new_file:
        new_file.write(redacted_content)
    
    return new_file_path

def main():
    """
    Main function that processes the file.
    >>> main()  # assuming user inputs 'psalm.txt' and 'love' in appropriate prompts
    REDACTED-psalm.txt shows "XXXX" instead of every occurrence of "love".
    """
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
