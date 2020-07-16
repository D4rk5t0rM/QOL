#!/bin/python3
import pyperclip as clip
import keyboard
tmpClip = clip.paste()
tmpClip2 = ""
mem = []
counter =0
def Print(value,counter):
    print('-'*100+'\n')
    print(str(counter) + " "*5 + "|"+ " "*5 + value + '\n')
    print('-'*100+'\n')

while True:
    #WIP
    #key = keyboard.read_key()
    #print(key)
    key = ""
    if tmpClip != tmpClip2:
        mem.append(tmpClip)
        Print(tmpClip,counter)
        tmpClip2 = tmpClip
        counter += 1

    #Commands:
    if key == 'esc':
        command = input()
        if command[0] == "show":
            print(mem[command[1]])
        if command[0] == "copy":
            clip.copy(mem[command[1]])
    tmpClip = clip.paste()
