import subprocess
import os


def exec_cmd(command):
    try:
        subprocess.run(command, shell=True).stdout
        return 0
    except:
        return 1


def print_state(program_file, message):
    print(program_file+', State: '+message)


def check_program(program_file, answer_file):

    print_state(program_file, 'Starting build...')
    if exec_cmd('gcc '+program_file) == 1:
        print_state(program_file, 'Build Exception')
        return 1

    print_state(program_file, 'Checking operation...')
    if exec_cmd('a.exe<input>program_tmp_output') == 1:
        print_state(program_file, 'Operation Check Exception')
        return 1

    print_state(program_file, 'Checking output...')
    if exec_cmd('fc program_tmp_output '+answer_file) == 1:
        print_state(program_file, 'Output Check Exception')
        return 1


list_dir = os.listdir()
files = [f for f in list_dir if os.path.isfile(os.path.join('.', f))]
programs = [p for p in files if p[-2:] == '.c']

print('Target programs: '+', '.join(programs))

for program in programs:
    check_program(program, 'output')
