# 33.55 Lab A: Redact

## Write a simple Python 3 script that:

1. Prompts the user for a pathname (a simple filename will do, as long as the file is in the current directory).

2. Prompts the user for a word to redact (i.e., replace with the same number of Xs as the original
   word has letters) in the file's contents.

4. Lets the user know where the new (redacted) content can be found, and what the redacted word will be replaced with.

5. Puts a copy of the file's contents into a new file, with "REDACTED-" prepended to
   the filename (not the whole pathname), and every occurrence of the word to be redacted
   (regardless of case, even in the middle of another word) appropriately replaced by the
   correct number of Xs.

Leave everything in the folder named "files" alone. It's used for testing, and your tests may not pass if you modify those files in any way.
