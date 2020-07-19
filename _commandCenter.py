#!/bin/python3

'''
#Notes: Problem with this script might be that it doesn't have a GUI so opening a new shell does not really work.
Need to work on this more.


THIS FILE IS A WIP AND DOES NOT WORK YET!!!
'''
import os
from os import listdir
from os.path import isfile, join
from subprocess import Popen

def main():
    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    #delete non python files:
    for i, word in enumerate(onlyfiles):
        # print(word)
        if word[-3:]!='.py':
            onlyfiles.pop(i)
        if word=='_commandCenter.py':
            onlyfiles.pop(i)
    onlyfiles.remove('_commandCenter.py')

    #print list:
    print("What file do you want to run? (select the number): ")
    for i, word in enumerate(onlyfiles):
        print("[{}] : {}".format(i, word))

    #select file:
    try:
        selection = int(input())
    except:
        print("something went wrong, using the first file for failsafe...")
        selection = 1
    runFile = onlyfiles[selection]
    Popen('python ' + runFile, shell=True)
    # exec(open(runFile).read()) # insecure
    # os.system('python '+ runFile) # insecure

while True:
    main()