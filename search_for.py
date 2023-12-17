#!/bin/python3
from platform import system
from sys import argv
from os import listdir
from os.path import isdir

if system() == 'Windows': slash = '\\'
else: slash = '/' # normal peoples slash

# file extensions that will be scaned
extens = ['.yml', '.dm']

# scan file for target
def search_file(path):
    file = open(start_path+path)
    lines = file.readlines()
    file.close()
    for i in lines:
        if target in i: print(f'📄 founded in {path} on {lines.index(i)} line')

# scan directory
def search_dir(path=''):
    files = listdir(start_path+path)
    for i in files:
        if i.endswith(tuple(extens)): search_file(path+i)
        elif isdir(start_path+path+i): search_dir(path+i+slash)
        elif target in i: print(f'🆔 founded in file name: {path}')

def main():
    print(f'running on {system()} with arguments: ' + ', '.join(argv))
    
    # user input
    # start_path - path to the directory from which script will start scanning
    # target - name, string, number, any symbol for search
    if len(argv) > 2: start_path, target = argv[1], argv[2]
    else: start_path, target = input('start from: '), input('target: ')
    
    print(f'\nsearching for {target} in {start_path}\n')
    search_dir()

    if system() == 'Windows': input() # if someone doubleclicked it on windows shitty microsoft terminal can just close it
    else: print()

if __name__ == '__main__': main()
