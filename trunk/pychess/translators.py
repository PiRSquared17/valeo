#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import urlopen
import re, os

FILENAME = 'TRANSLATORS'
if os.path.exists(FILENAME): os.remove(os.path.join(FILENAME))
print "Getting data from Rosetta Launchpad..."
data = urlopen('http://translations.launchpad.net/pychess/trunk/+translations').read()
langs = re.findall('/pychess/trunk/\+pots/pychess/(.*?)/\+translate', data)
langs.sort()

for lang in langs:
    site = "https://translations.launchpad.net/pychess/trunk/+pots/pychess/%s/+translate" % lang
    data = urlopen(site).read()
    language = re.findall("<h1>Browsing (.*?) translation</h1>", data)[0]
    start = data.find('Contributors to this translation')
    pers = re.findall('class="sprite person">(.*?)</a>', data[start:])
    with open(FILENAME,'a') as file:
        print >> file, "[%s] %s" % (lang, language)
        print "Did", language
        for per in pers:
            print >> file, "     " + per
        print >> file
