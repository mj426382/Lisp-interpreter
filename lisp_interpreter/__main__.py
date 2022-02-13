import sys
from function import parse_function

def run_lisp_file(fileName):
    file = open(fileName, 'r')
    fileContent = file.read()
    return parse_function(fileContent)

if __name__ == '__main__':
    lisp_programs_to_run = sys.argv[1:len(sys.argv)]
    for program in lisp_programs_to_run:
        program_out = run_lisp_file(program)
        print(program + ': ' + str(program_out) + '\n')
