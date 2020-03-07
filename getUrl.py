import os

import requests
from bs4 import BeautifulSoup


def get_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")


    file = open("link.txt",'w',encoding='utf-8') 

    for link in soup.find_all('li', class_="cat-item"):
        s = link.a.get('href')
        file.write(s+'\n')
    file.close()

    file = open("last.txt",'w',encoding='utf-8') 
    file.write('0')
    file.close

