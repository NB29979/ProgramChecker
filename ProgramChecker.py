import subprocess


def build_check():
    print('starting build...')
    try:
        res = subprocess.run('gcc HelloWorld.c', shell=True)
        print(res)
        return 0
    except:
        print('build exception')
        return 1


def operation_check():
    print('operation check...')
    try:
        res = subprocess.run('a.exe < input', shell=True,stdout=subprocess.PIPE)
        print(res)
        # TODO:outputと比較
        return 0
    except:
        print('operation check failed')
        return 1


def


if build_check() == 0:
    operation_check()
