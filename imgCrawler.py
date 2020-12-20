#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup
from tqdm import tqdm
import wget

url = sys.argv[1]
if url == "":
  print("Please paste the URL of the website: ")
  while url=="":
    print("Something went wrong, please try again...")
    url = input()
#Single base URL request:
r = requests.get(url)

if r.status_code == 200:
  page = r.text
  soup = BeautifulSoup(page, 'html.parser')
  imgTag = soup.findAll('img')
  
  for i in tqdm(imgTag, "Downloading images..."):
    img = i['src']
    image = wget.download(img)
