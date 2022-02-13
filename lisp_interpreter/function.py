import copy

from list import parse_list

functions = {}

def calculate_function(function_list, is_declaration):
    function_name = function_list[1]
    if not function_name in functions:
        functions[function_name] = function_list
    if function_name == 'main' or not is_declaration:
        for i in range(3, len(function_list)):
            from command import calculate_command_list
            function_list[i] = calculate_command_list(function_list[i])
    return function_list[len(function_list) - 1]

def replace_argument_with_value(function_list, argument, value, start):
    for i in range(start, len(function_list)):
        if isinstance(function_list[i], list):
            function_list[i] = replace_argument_with_value(function_list[i], argument, value, 0)
        elif function_list[i] == argument:
            function_list[i] = value
    return function_list

def execute_function(function_list):
    function_name = function_list[0]
    function_parameters = function_list[1: len(function_list)]
    if not function_name in functions:
        raise Exception('Declare function before execution!')
    function_definition_list = copy.deepcopy(functions[function_name])
    function_definition_list = function_definition_list[1:len(function_definition_list)]
    function_definition_parameters = function_definition_list[1]
    for i in range(0, len(function_definition_parameters)):
        function_definition_list = replace_argument_with_value(function_definition_list, function_definition_parameters[i], function_parameters[i], 2)
    function_definition_list.insert(0, 'defun')
    return calculate_function(function_definition_list, False)


def parse_function(text):
    function_list = parse_list(text)
    return calculate_function(function_list, True)
