"""
Program: LAB A Redact
Author: Eliel Cortes
Professor: Prof. Ordonez
Date: 2024-11-07
"""
import os
def read_file(filename):
    """Reads the content of file if it exists"""
    directory = '/Users/eliel/CPTR 215/Week 10/LAB A Redact/files'
    filepath = os.path.join(directory, filename)
    
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: {filename} not found in {directory}.")
        return None

    with open(filepath, 'r') as f:  # Use the correct filepath
        content = f.read().strip().split()
    return content

def redact_word(content, word_to_redact):
    """
    Redacts a word by replacing it with 'x' into the content list.
    """
    redacted_content = ['x' * len(word_to_redact) if word == word_to_redact else 
                        word for word in content]
    return redacted_content

def redacted_file(filename, redacted_content, word_to_redact):
    """
    Writes the redacted content into the filename
    """
    with open(filename, 'w') as f:
       f.write(" ".join(redacted_content))
    print(f'REDACTED-{filename} shows \"{'X' * len(word_to_redact)}\" instead of every occurrance of \"{word_to_redact}\".')
    

def main():
    filename = input("Path to file: ")
    word_to_redact = input("Word to redact: ")

      # Use the functions to process the input
    content = read_file(filename)
    if content is None:
        return 
    redacted_content = redact_word(content, word_to_redact)
    redacted_file(filename, redacted_content, word_to_redact)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

    
    


