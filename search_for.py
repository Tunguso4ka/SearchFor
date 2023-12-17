#!/bin/python3
from platform import system
from sys import argv
from os import listdir
from os.path import isdir

if system() == 'Windows': slash = '\\'
else: slash = '/' # normal peoples slash

# this scripts localization
language = 'enUS'
locale = {}
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

# import locale dictionary with strings
def load_locale():
    global locale
    locale = __import__('loc.enUS', fromlist=[' ']).locale #fallback locale
    if language != 'enUS': locale |= __import__('loc.'+language, fromlist=[' ']).locale

def main():
    load_locale()
    print(locale['running'].format(system()) + ', '.join(argv))
    
    # user input
    # start_path - path to the directory from which script will start scanning
    # target - name, string, number, any symbol for search
    if len(argv) > 2: start_path, target = argv[1], argv[2]
    else: start_path, target = input(locale['start_path_input']), input(locale['target_input'])

    if target == '':
        print(locale['empty_target'])
        return

    print(locale['searching'].format(target, start_path))
    search_dir()

    if system() == 'Windows': input() # if someone doubleclicked it on windows shitty microsoft terminal can just close it
    else: print()

if __name__ == '__main__': main()
