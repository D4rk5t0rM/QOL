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
    counter = 245

    print("how many items?...")
    try:
        items = int(input())
    except:
        print("somethign went wrong... \ngoing further with the value of 10 items....")
        items = 10

    for i in range(0,items):
        print("Processing number: "+ str(i) )
        #package select:
        move(200, counter)
        
        #select prefix
        move(447,309)
        pyautogui.write('IM')
        
        #select tag
        move(567,502)
        move(770, 504)
        move(74, 374)
        move(433, 383) 
        
        #package update
        counter += 17
    move(230,133)
    print("done!")

#---------#
main()
    