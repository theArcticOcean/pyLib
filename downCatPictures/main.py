#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import requests
import urllib.request
import os
from urllib.request import urlretrieve
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def check_folder( folderName ):
    if False == os.path.exists( folderName ):
        os.mkdir( folderName )

def request_download( IMAGE_URL, folderName ):
    fileName = IMAGE_URL.split('/')[-1] #fetch last one
    print( IMAGE_URL + ' => ' + fileName )
    r = requests.get( IMAGE_URL )
    with open( folderName + '/' + fileName, 'wb' ) as f:
        f.write( r.content )
        f.close()

def getHtml( url ):
    # chrome_headers =  ...
    page1 = urllib.request.Request( url, headers=chrome_headers )
    page = urllib.request.urlopen( page1 )
    html = page.read()
    return html

if __name__ == '__main__':
    folderName = 'CatImages'
    check_folder( folderName )
    URLs = [ 'https://www.hippopx.com/zh/search?q=%E7%8C%AB',
             'https://www.hippopx.com/zh/search?q=%E7%8C%AB&page=2',
             'https://www.hippopx.com/zh/search?q=%E7%8C%AB&page=3',
             'https://www.hippopx.com/zh/search?q=%E7%8C%AB&page=4',
             'https://www.hippopx.com/zh/search?q=%E7%8C%AB&page=5']
    for url in URLs:
        html = getHtml( url )
        bs = BeautifulSoup( html, 'html.parser' )
        images = bs.findAll( 'img', { 'itemprop': 'contentUrl' } )
        for image in images:
            image_url = image.attrs['src']
            request_download( image_url, folderName )
