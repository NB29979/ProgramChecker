import subprocess


def exec_cmd(command):
    try:
        res=subprocess.run(command,shell=True).stdout
        print(res)
        return 0
    except:
        return 1


def check_program(program_file, answer_file):

    print('State: Starting build...')
    if exec_cmd('gcc '+program_file) == 1:
        print('build exception: '+program_file)
        return 1

    print('State: Checking operation...')
    if exec_cmd('a.exe<input>program_tmp_output') == 1:
        print('operation check exception: '+program_file)
        return 1

    print('State: Checking output...')
    if exec_cmd('fc program_tmp_output '+answer_file) == 1:
        print('output check exception: '+program_file)
        return 1


check_program('HelloWorld.c', 'output')
