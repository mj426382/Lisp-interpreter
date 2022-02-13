import numpy as np

from constants import disallowed_atom_chars

def is_atom(text):
    text = str.strip(text)
    return not np.in1d(text, disallowed_atom_chars)

def parse_atom(text):
    text = str.strip(text)
    if text == '': 
        raise Exception('Atom can not be empty!')
    if not is_atom(text):
        raise Exception('Atom can not contain all characters')
    if text == 'false':
        return False
    elif text == 'true':
        return True
    elif text.isnumeric():
        return int(text)
    return text
