# -*- coding: utf-8 -*-
'''
First download "Picture of the Day" from http://commons.wikimedia.org/wiki/Commons:Picture_of_the_day
and write watermark say: "Wikimedia Commons"

Do you need wikipedia.py module, see: http://svn.wikimedia.org/svnroot/pywikipedia/trunk/pywikipedia
'''

from wikipedia import Site, Page, ImagePage
from PIL import Image, ImageDraw, ImageFont
import httplib, time, sys, os
import ctypes, win32con

def get_commons_image(image):
    headers = {"Accept": "image/jpg",
               "Accept": "image/gif",
               "Accept": "image/png",
               }
    conn = httplib.HTTPConnection('upload.wikimedia.org')
    conn.request("GET", image, None, headers)
    r = conn.getresponse()
    data = r.read()
    arq = open("Picture_of_the_day.bmp","wb") # convert image "on the fly" to Windows Bitmap
    arq.write(data)
    arq.close()
    conn.close()

def write_gray(filename, text, outfilename):
    img = Image.open(filename).convert("RGB")
    write = Image.new("RGB", (img.size[0], img.size[1]))
    draw = ImageDraw.ImageDraw(img)
    size = 0
    while True:
        size +=1
        FONT = "C:\WINDOWS\Fonts\Verdana.ttf"
        nextfont = ImageFont.truetype(FONT, size)
        nexttextwidth, nexttextheight = nextfont.getsize(text)
        if nexttextwidth+nexttextheight/3 > write.size[0]: break
        font = nextfont
        textwidth, textheight = nexttextwidth, nexttextheight
    draw.setfont(font)
    draw.text(((write.size[0]-textwidth)/55, (write.size[0]-textheight)/55), text, fill=(120,120,120))
    img.save(outfilename)
    
if __name__ == '__main__':
    
    commons = Site('commons', 'commons')
    date_today = time.strftime('%Y-%m-%d', time.localtime())
    template = 'Template:Potd/%s' % date_today
    templatePage = Page(commons, template)
    image_today = templatePage.get()
    image_name = 'Image:%s'% image_today
    imageURL = ImagePage(commons, image_name)
    featuredImage = imageURL.fileUrl()
    image = featuredImage[27:]
    
    get_commons_image(image)

    write_gray('Picture_of_the_day.bmp',
               'Wikimedia Commons',
               'Picture_of_the_day.bmp')
