#!/bin/python3
import pyautogui

def debug(): #debug option to print the mouse position, call debug() to activate
    x, y = pyautogui.position()
    print('X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4))

def move(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def main():
    #used for selecting the right package in the list.
    counter = 190

    print("how many items?...")
    try:
        items = int(input())
    except:
        print("somethign went wrong... \ngoing further with the value of 10 items....")
        items = 10

    for i in range(0,items):
        print("Processing number: "+ str(i) )
        #package select:
        move(100, counter)
        
        #select prefix
        move(333,256)
        pyautogui.write('IM')
        
        #select tag
        move(320,444)
        move(1668, 449)
        move(37, 374)
        move(445, 375) 
        
        #package update
        counter += 17
    move(120,57)
    print("done!")

#---------#
main()
    