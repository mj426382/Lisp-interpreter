from list import parse_list
from operation import calculate_operation_list 

def calculate_condition(condition_list):
    bool_value = calculate_operation_list(condition_list[1])
    value_to_return = condition_list[3]
    if bool_value:
        value_to_return = condition_list[2]
    from command import calculate_command_list
    return calculate_command_list(value_to_return)

def parse_condition(text):
    condition_list = parse_list(text)
    return calculate_condition(condition_list)
