# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import re
import csv


def exec_cmd(command, failed_message):
    try:
        res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if res.stderr == '':
            print(res.stdout, end='')
            return res.stdout
        else:
            print(res.stderr, end='')
            print(failed_message)
            return 1
    except subprocess.CalledProcessError:
        print('Command Exception', end='')


def check_program(program_file, input_file, answer_file):
    print(program_file)
    print('Starting build...')
    if exec_cmd('gcc '+program_file, 'Build Failed') == 1 : return 1

    print('Checking operation...')
    if exec_cmd('a.exe<'+input_file+'>program_tmp_output', 'Operation Failed') == 1:return 1

    print('Checking output...')
    if exec_cmd('fc program_tmp_output '+answer_file, 'Output Failed') == 1:return 1


def disp_program(program_file):
    print('-*-*-*-*-*-\n')
    exec_cmd('type '+program_file, 'Program file cannot open...')
    print('\n\n-*-*-*-*-*-')


def record_results(question, results):
    try:
        with open(question+'_results.csv', 'w')as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            for result in results:
                writer.writerow(result)

    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)


question = sys.argv[1]
results = []
target_dir = '.\\'+question+'\\'
list_dir = os.listdir(target_dir)
files = [f for f in list_dir if os.path.isfile(os.path.join(target_dir, f))]

programs = [target_dir+p for p in files if p[-2:] == '.c' or p[-4:] == '.cpp']
input_file = target_dir+'_input'
output_file = target_dir+'_output'

print('Target programs: '+', '.join(programs))

for program in programs:
    score = 0
    print('\n\n------^------^------^------')
    check_program(program, input_file, output_file)
    disp_program(program)

    ID = program.split('_')[1]

    print(program)
    print('現在の学籍番号: '+ID)

    score = int(input('得点 >'))
    print(program+' : [.c], 得点-> ', end='')
    if program[-2:] != '.c': score -= 1
    print(score)

    results.append([ID, score])

record_results(question, results)
