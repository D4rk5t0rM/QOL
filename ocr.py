#!/bin/python3
'''
todo: make sure that from left to right screenshot works too


dependencies:
    pip install tesseract
    pip install tesseract-ocr
    MS visual studio - for Microsoft Visual C++ 14.0
'''


import pyscreenshot as scrn
from pynput import mouse
import keyboard
import pytesseract as ocr
from PIL import Image

coord=list()
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        # print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
        if pressed ==True:
            coord.append(x)
            coord.append(y)
        else:
            coord.append(x)
            coord.append(y)

        if len(coord)%4 == 0:

            a = 1/0 #will throw an exception so we return to the main function
            print(a) # to get the warning to go away, this will not do anything actually.

def main():
    if keyboard.is_pressed('alt') & keyboard.is_pressed('p'):
        print('taking screenshot...')
        # while i <2:
        try:
            listener = mouse.Listener(on_click=on_click)
            listener.start()
            listener.join()
        except:
            print('jump')

        #fill values
        x1 = coord[len(coord)-4]
        y1 = coord[len(coord)-3]
        x2 = coord[len(coord)-2]
        y2 = coord[len(coord)-1]

        #check values are good for use
        if x1 > x2:
            x1 = coord[len(coord)-2]
            x2 = coord[len(coord)-4]
        if y1 > y2:
            y1 = coord[len(coord)-1]
            y2 = coord[len(coord)-3]

        #take screenshot
        img = scrn.grab(bbox=(x1,y1,x2,y2))
        #img.show()
        img.save('ocr.png')
        # img1 = Image.open("ocr.png")
        # text = ocr.image_to_string(img1)
        text = ocr.image_to_string(img)

        print(text)

while True:
    main()