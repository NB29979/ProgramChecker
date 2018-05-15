import subprocess
import os
import re


def exec_cmd(command, failed_message):
    try:
        res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if res.stderr == '':
            print(res.stdout)
            return res.stdout
        else:
            print(res.stderr)
            print(failed_message)
            return 1
    except subprocess.CalledProcessError:
        print('Command Exception')


def check_program(program_file, input_file, answer_file):
    print(program_file)
    print('Starting build...')
    if exec_cmd('gcc '+program_file, 'Build Failed') == 1 : return 1

    print('Checking operation...')
    if exec_cmd('a.exe<'+input_file+'>program_tmp_output', 'Operation Failed') == 1:return 1

    print('Checking output...')
    if exec_cmd('fc program_tmp_output '+answer_file, 'Output Failed') == 1:return 1


def disp_program(program_file):
    print('-*-*-*-*-*-')
    exec_cmd('type '+program_file, 'Program file cannot open...')
    print('-*-*-*-*-*-\n')


target_dir = '.\\kadai01\\'
list_dir = os.listdir(target_dir)
files = [f for f in list_dir if os.path.isfile(os.path.join(target_dir, f))]
programs = [p for p in files if p[-2:] == '.c' or p[-4:] == '.cpp']

print('Target programs: '+', '.join(programs))

for program in programs:
    score = 0
    print('------')
    check_program(target_dir+program, target_dir+'kadai01_input', target_dir+'kadai01_output')
    disp_program(target_dir+program)

    ID = exec_cmd('findstr /R  [0-9][0-9] '+target_dir+program, 'Finding ID Failed')
    m = re.search(r'[0-9]{10}', ID)
    if m: ID = m.group(0)
    else: ID = 'NaN'

    print('現在の学籍番号: '+ID)
    id_input = input('学籍番号（変更しない場合Enter）>')
    if id_input != '': ID = id_input
