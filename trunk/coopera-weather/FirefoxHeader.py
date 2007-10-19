#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import *

# Mozilla Firefox for open weather.com
class Firefox(URLopener):
    version = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20061201 Firefox/2.0.0.3 (Ubuntu-feisty)"
    def __init__(self, *args):
        URLopener.__init__(self)
_urlopener = Firefox()

