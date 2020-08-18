# Given a string, detect whether or not it is a pangram. 
# Return True if it is, False if not. 
# Ignore numbers and punctuation.

import string
from string import ascii_lowercase

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chars = list(filter(lambda x: x in ascii_lowercase,s.lower()))
    for i in alphabet:
        if i not in chars:
            return False
    return True

is_pangram("The quick, brown fox jumps over the lazy dog!") # True