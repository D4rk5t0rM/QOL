#!/bin/python3
from pynput import mouse
import keyboard

writeFile = ''
sleep =0

def globalFile(fileName, Sleep):
    global writeFile
    global sleep
    writeFile = fileName
    sleep = Sleep

def on_click(x, y, button, pressed):
    f = open(writeFile, 'a')
    if button == mouse.Button.left:
        if pressed:
            #left button is pressed            
            f.write(' ' * 4 + 'move({},{})\n    time.sleep({})\n'.format(x,y,sleep))
            print('written x={} & y={} to file...'.format(x,y))

    if x == 0 & y == 0:
        f.write('\n    print("sleeping for 5 sec...")\n    time.sleep(5)\n')
        f.close()
        print('closing up...')
        return False
    else:
        pass

def checkFile(writeFile):
    try:
        f = open(writeFile, 'x')
        f.close()
    except:
        print('existing file found do you want to overwrite it? (yes/y | no/n)...')
        inp = input()
        if inp == 'yes' or inp == 'y':
            f = open(writeFile, 'w')
            f.write('')
            f.close()
        else:
            print(inp)
            exit()

def main():

    print('Name of the new python file:')
    fileName = input() +'.script.py'
    print('How many secs wait between each click?: default = 0...')
    try:
        sleep = int(input())
    except:
        print("there is an error: default 0")
        sleep = 0
    globalFile(fileName,sleep)
    checkFile(writeFile)

    f = open(writeFile, 'a')
    f.write("#!/bin/python3\nimport pyautogui, time\n\ndef move(x,y):\n    pyautogui.moveTo(x, y)\n    pyautogui.click()\n\ndef main():\n    pyautogui.FAILSAFE = False\n")
    f.close()
    
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()

    f = open(writeFile,'a')
    f.write("\nmain()")
    f.close() 
    

#---------#
main()