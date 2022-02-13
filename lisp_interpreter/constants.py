whitespaces = [' ', '\t', '\n', '\r']
disallowed_atom_chars = whitespaces.extend(['(', ')'])
arithmetic_operators = ['+', '-', '*', '/', 'mod']
logical_operators = ['and', 'or', 'not']
comparison_operators = ['==', '/=', '<', '>', '<=', '>=', 'max', 'min']
all_operators = logical_operators + arithmetic_operators + comparison_operators
