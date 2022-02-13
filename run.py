import sys
import os

def run_examples():
    directory = os.fsencode('lisp_examples')

    for root, dirs, files in os.walk(directory):
        for filename in files:
            path = str(os.path.join(root, filename))
            os.system('python3 lisp_interpreter ' + path[2: len(path)-1])

if __name__ == '__main__':
    programs_to_run = sys.argv[1:len(sys.argv)]
    if programs_to_run[0] == 'run_examples':
        run_examples()
    elif programs_to_run[0] == 'test':
        os.system('python3 lisp_interpreter/tests.py')
    elif programs_to_run[0] == 'run':
        file_name = programs_to_run[1]
        os.system('python3 lisp_interpreter lisp_programs/' + file_name)
