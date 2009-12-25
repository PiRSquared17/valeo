#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Based on software "Desktop Wallpaper Love"
http://code.google.com/p/ngwallpaper/

'''

import os, re, urllib2
import win32api, win32gui, win32con
from PIL import Image, ImageDraw, ImageFont

from time import sleep
sleep(60)

class DesktopWallpaper:
    def __init__(self, proxy=None):
        if proxy:
            PROXY_IP = proxy['IP']
            PROXY_USER = proxy['USER']
            PROXY_PASSWORD = proxy['PASSWORD']
            PROXY_PORT = proxy['PORT']

            proxy_url = 'http://' + PROXY_USER + ':' + PROXY_PASSWORD + \
                '@' + PROXY_IP + ':' + PROXY_PORT
            proxy_support = urllib2.ProxyHandler({'http': proxy_url})
            opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
            urllib2.install_opener(opener)

    def readnatgeo(self):
        SITEURL = 'http://www.nationalgeographic.com/photography/today/'
        req = urllib2.Request(SITEURL)
        data = urllib2.urlopen(req).read()

        p = re.compile('/photography/wallpaper/.*\\.html')
        m = p.search(data)

        WP_URL = 'http://photography.nationalgeographic.com' + str(m.group())
        req = urllib2.Request(WP_URL)
        data = urllib2.urlopen(req)
        content = data.read()
        return content

    def lookforwallpaper(self, content):
        lookfor = re.compile('href="(\\S*-lw\\.jpg)')
        picture = lookfor.search(content).group(1)
        wallpaper = 'http://photography.nationalgeographic.com' + str(picture)
        return wallpaper

    def downloadjpg(self, wallpaper):
        req = urllib2.Request(wallpaper)
        data = urllib2.urlopen(req).read()
        jpgimgfile = 'wallpaper.jpg'
        imgfile = open(jpgimgfile, 'wb')
        imgfile.write(data)
        imgfile.close()
        path = os.getcwd() + os.sep + jpgimgfile
        return path
    
    def downloadbmp(self, wallpaper):
        req = urllib2.Request(wallpaper)
        data = urllib2.urlopen(req).read()
        imgfile = open('wallpaper.jpg', 'wb')
        imgfile.write(data)
        imgfile.close()
        bmpimgfile = 'wallpaper.bmp'
        Image.open('wallpaper.jpg').save(bmpimgfile, 'BMP')
        path = os.getcwd() + os.sep + bmpimgfile
        return path

    def write_gray(self, path1, text, path):
        img = Image.open(path1).convert("RGB")
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
        img.save(path)
    
    def setwallpwindows(self, path):
        self.write_gray(path, 'www.nationalgeographic.com/photography/today', path)
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, 'WallpaperStyle', 0, win32con.REG_SZ, '0')
        win32api.RegSetValueEx(k, 'TileWallpaper', 0, win32con.REG_SZ, '0')
        win32api.RegSetValueEx(k, 'Wallpaper', '0', win32con.REG_SZ, path)

def run(proxy=None):
    wallp = DesktopWallpaper(proxy)
    content = wallp.readnatgeo()
    wallpaper = wallp.lookforwallpaper(content)
    storebmp = wallp.downloadbmp(wallpaper)
    wallp.setwallpwindows(storebmp)

if __name__ == '__main__':
    run()
