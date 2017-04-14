# coding=utf-8
import urllib

import requests
from bs4 import BeautifulSoup
def download_picture(url):
    picturename=url.split('/')[-1]
    # url='http://media-mcw.cursecdn.com/3/3f/Beta.png'
    g = urllib.request.urlopen('http://media-mcw.cursecdn.com/3/3f/Beta.png')
    with open(picturename, 'b+w') as f:
        f.write(g.read())

if __name__ == '__main__':
    url='http://media-mcw.cursecdn.com/3/3f/Beta.png'
    download_picture(url)