from atom import parse_atom
from constants import whitespaces

def is_list(text):
    itter = 0
    left_brackets_number = 0
    right_brackets_number = 0
    for char in text:
        if char == '(':
            left_brackets_number += 1
        elif char == ')':
            right_brackets_number += 1
        if right_brackets_number > left_brackets_number:
            return False
        itter += 1
    return True


def add_atom_to_list(result_list, atomString):
    result_list.append(parse_atom(atomString))
    return result_list

def parse_list_recursive(text, itter):
    result_list = []
    current_atom_string = ''
    while itter < len(text):
        if text[itter] == '(':
            smaller_result = parse_list_recursive(text, itter + 1)
            itter = smaller_result[0] - 1
            result_list.append(smaller_result[1])
        elif text[itter] == ')':
            if current_atom_string != '':
                result_list = add_atom_to_list(result_list, current_atom_string)
            return [itter + 1, result_list]
        elif text[itter] in whitespaces:
            if current_atom_string != '':
                result_list = add_atom_to_list(result_list, current_atom_string)
            current_atom_string = ''
        else:
            current_atom_string += text[itter]
        itter += 1
    return [itter, result_list]

def parse_list(text):
    if len(text) == 0:
        raise Exception('List can not be empty!')
    list = str.strip(text)
    if list[0] != '(':
        raise Exception('List has to start with "("!')
    if not is_list(text):
        raise Exception('List can not have incorrect parenthetical expression!')
    result_list = parse_list_recursive(text, 1)
    return result_list[1]
 