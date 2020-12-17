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
    counter = 332

    print("how many items?...")
    try:
        items = int(input())
    except:
        print("somethign went wrong... \ngoing further with the value of 10 items....")
        items = 10

    for i in range(0,items):
        print("Processing number: "+ str(i) )
        #package select:
        move(229, counter)
        
        #select prefix
        move(571,439)
        pyautogui.write('IM')
        
        #select tag
        move(725,778)
        move(3396, 775)
        move(84, 660)
        move(787, 662) 
        
        #package update
        counter += 30
    move(200,108)
    print("done!")

#---------#
main()
    