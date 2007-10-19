#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
import sys

from FirefoxHeader import *
from libcoopera import WeatherChannel, OfflineIcon
try:
    import pygtk, gtk
    pygtk.require('2.0')
except ImportError:
    print "Coopera Weather require GTK and PyGTK installed in your machine."
    sys.exit()

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
