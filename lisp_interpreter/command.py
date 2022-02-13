from constants import all_operators
from function import functions
from function import calculate_function, execute_function
from condition import calculate_condition
from operation import calculate_operation_list

def calculate_command_list(command_list):
    if not isinstance(command_list, list):
        return command_list
    elif command_list[0] == 'if':
        return calculate_condition(command_list)
    elif command_list[0] == 'defun':
        return calculate_function(command_list, True)
    elif command_list[0] in all_operators:
        return calculate_operation_list(command_list)
    elif command_list[0] in functions.keys():
        return execute_function(command_list)
    else:
        return command_list
