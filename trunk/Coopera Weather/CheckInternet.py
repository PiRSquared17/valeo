#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
from FirefoxHeader import *
from libcoopera import *
import gtk

def main():
    try:
        url = 'http://www.google.com'
        html = urlopen(url).read()
        check = True
    except:
        check = False
    if check == True:
        WeatherChannel()
        gtk.main()
    else:
        OfflineIcon()
        gtk.main()
