# QOL
Quality of life improvemnts; A repo filled with scripts that can automate certain tasks and generally improve PC usage.

# Installation
Clone the whole repo:
```git clone https://github.com/D4rk5t0rM/QOL.git```
Install only the scripts you want:
```wget https://raw.githubusercontent.com/D4rk5t0rM/QOL/master/LICENSE```
(or use any other you know of cloning a repo/file)

# Scripts
## _commandCenter.py
A WIP python script that should be able to spawn a new shell to run antoher python script in, this way you could summon every python program in this repo from one script.

## cliplog.py
A python script that keeps a log of your clipboard data, only for as long as the script is running. This makes it easy to get previous copied content back.

## mousePosition.py
A quick and dirty script that prints the position of the mouse after every click. This can be usefull to find the x&y coördinates on the screen

## dazContentPackageAssist.py
An automated way to select a few settings in the program 'Content Package Assist' for DAZ studio.

## ocr.py
Python script that makes OCR possible by selecting an area on screen. will output the OCR text data to the shell. (dependency tesseract should be installed and added to your path variable to make it work. default ocr screenshot hotkey is <alt + p>

## ReverseImageAutomation.py
A Python script that makes reverse image searching a bit easier. It will automate the search of various sites so you don't have to go to them one by one.
you can either paste the URL in an input screen or let the script copy a URL of a picture from the clipboard

## requirements.txt
run ```pip3 install -r requirements.txt``` to install python inmports by all these scripts.

## tts.py
A python script that turns a 'transcript.speak' file from the same folder into a MP3 file + Every line from the file will also get it's own mp3 file.

## imgCrawler.py
A ptyhon script that crawls a webpage for all the images on the page and downloads them

## OpenUrl.py
A python script that will open urls that are spcified in a file called URL.txt
