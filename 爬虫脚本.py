#!/usr/bin/python
# coding=utf-8

import urllib
import urllib2
import os
from bs4 import BeautifulSoup
import sys


def getImage(url, filePath):

    reload(sys)
    sys.setdefaultencoding('utf-8')
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    result = soup.findAll(attrs={'class': 'post-body'})
    # print(result)

    for li in result:
        imageArray = soup.findAll('img')

        for image in imageArray:
            link = image.get('src')
            name = image.get('alt')

            if not os.path.exists(filePath):
                os.mkdir(filePath)

            filesavepath = '/Users/akring/Desktop/pic/%s.png' % name

            if os.path.exists(filesavepath) and os.path.isfile(filesavepath):
                # pos = filesavepath.find(".png")
                # filesavepath = filesavepath[:pos] + "附件" + filesavepath[pos:]
                print ("File already exists")
                break
            print link
            urllib.urlretrieve(link, filesavepath)

if __name__ == '__main__':

    print("start")

    url = 'http://akring.github.io/2014/05/29/mac%E4%B8%8B%E7%9A%84%E5%88%87%E5%9B%BE%E7%A5%9E%E5%99%A8%E2%80%94%E2%80%94slicy%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/'
    filePath = '/Users/akring/Desktop/pic'

    getImage(url, filePath)
