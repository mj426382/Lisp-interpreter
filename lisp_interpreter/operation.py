from list import parse_list
from constants import all_operators, arithmetic_operators, logical_operators, comparison_operators

def count_arithmetic_list(operator, result, simplier_list):
    if operator == '+':
        for element in simplier_list:
            result += element
    elif operator == '-':
        for element in simplier_list:
            result -= element
    elif operator == '*':
        for element in simplier_list:
            result *= element
    elif operator == '/':
        for element in simplier_list:
            result /= element
    elif operator == 'mod':
        for element in simplier_list:
            result %= element
    return result

def count_logical_list(operator, result, simplier_list):
    if operator == 'and':
        for element in simplier_list:
            result = result and element
    elif operator == 'or':
        for element in simplier_list:
            result = result or element
    elif operator == 'not' and len(simplier_list) == 0:
        result = not result
    return result

def count_comparison_list(operator, result, simplier_list):
    size = len(simplier_list)
    if operator == '==' and size == 1:
        result = result == simplier_list[0]
    elif operator == '/=' and size == 1:
        result = result != simplier_list[0]
    elif operator == '>' and size == 1:
        result = result > simplier_list[0]
    elif operator == '<' and size == 1:
        result = result < simplier_list[0]
    elif operator == '>=' and size == 1:
        result = result >= simplier_list[0]
    elif operator == '<=' and size == 1:
        result = result <= simplier_list[0]
    elif operator == 'min' and size == 1:
        result = min([result, simplier_list[0]])
    elif operator == 'max' and size == 1:
        result = max([result, simplier_list[0]])
    return result

def count_simple_list(simple_list):
    operator = simple_list[0]
    result = simple_list[1]
    if not operator in all_operators:
        from command import calculate_command_list
        return calculate_command_list(simple_list)
    simple_list = simple_list[2:len(simple_list)]
    if operator in arithmetic_operators:
        result = count_arithmetic_list(operator, result, simple_list)
    elif operator in logical_operators:
        result = count_logical_list(operator, result, simple_list)
    elif operator in comparison_operators:
        result = count_comparison_list(operator, result, simple_list)
    return result

def is_simple_operand_list(base_list):
    if not base_list[0] in all_operators:
        return False
    base_list = base_list[1: len(base_list)]
    for element in base_list:
        if not isinstance(element, int):
            return False
    return True

def calculate_operation_list(base_list):
    if len(base_list) < 2:
        raise Exception('Operation has to have at least 2 args!')
    itter = 1
    while itter < len(base_list):
        if isinstance(base_list[itter], int):
            itter += 1
            continue
        elif is_simple_operand_list(base_list[itter]):
            base_list[itter] = count_simple_list(base_list[itter])
        elif isinstance(base_list[itter], list):
            base_list[itter] = calculate_operation_list(base_list[itter])
        itter += 1
    return count_simple_list(base_list)

def parse_operation(text):
    operation_array = parse_list(text)
    if len(operation_array) < 2:
        raise Exception('Operation has to have at least 2 args!')
    if operation_array[0] in all_operators:
        return calculate_operation_list(operation_array)
