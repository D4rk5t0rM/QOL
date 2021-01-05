#!/usr/bin/python3

import webbrowser

f = open('./url.txt','r')
print(f)
for line in f:
    webbrowser.open_new_tab(line)