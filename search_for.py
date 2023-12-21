#!/bin/python3
from platform import system
from sys import argv
from os import listdir
from os.path import isdir, exists

if system() == 'Windows': slash = '\\'
else: slash = '/' # normal peoples slash

# localisation
locale = {
        'file_founded':'📄 founded in {0} on {1} line',
        'id_founded':'🆔 founded in file name: {0}',
        'running':'running on {0} with arguments: {1}',
        'start_path_input':'start from: ',
        'target_input':'target: ',
        'searching':'\nsearching for {0} in {1}\n',
        'empty_target':'target can`t be empty!',
        'path_wrong':'path "{0}" does not exists.'
        }
# file extensions that will be scaned
extens = ['.yml', '.dm']

# scan file for target
def search_file(path):
    file = open(start_path+path)
    lines = file.readlines()
    file.close()
    for i in lines:
        if target in i: print(locale['file_founded'].format(path, lines.index(i)))

# scan directory
def search_dir(path=''):
    files = listdir(start_path+path)
    for i in files:
        if i.endswith(tuple(extens)): search_file(path+i)
        elif isdir(start_path+path+i): search_dir(path+i+slash)
        elif target in i: print(locale['id_founded'].format(path))

def end():
    if system() == 'Windows': input('\nScript now can be closed.') # if someone doubleclicked it on windows shitty microsoft terminal can just close it
    else: print()
    exit()

def main():
    global start_path, target
    print(locale['running'].format(system(), ', '.join(argv)))
    
    # user input
    # start_path - path to the directory from which script will start scanning
    # target - name, string, number, any symbol for search
    if len(argv) > 2: start_path, target = argv[1], argv[2]
    else: start_path, target = input(locale['start_path_input']), input(locale['target_input'])

    if target == '':
        print(locale['empty_target'])
        end()
    if not exists(start_path):
        print(locale['path_wrong'].format(start_path))
        end()

    print(locale['searching'].format(target, start_path))
    search_dir()

    end()

if __name__ == '__main__': main()
