#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import urlopen
import re, codecs

data = urlopen('http://translations.launchpad.net/pychess/trunk/+translations').read()
langs = re.findall('/pychess/trunk/\+pots/pychess/(.*?)/\+translate', data)
langs.sort()

for lang in langs:
    site = "https://translations.launchpad.net/pychess/trunk/+pots/pychess/%s/+translate" % lang
    data = urlopen(site).read()
    language = re.findall("<h1>Browsing (.*?) translation</h1>", data)[0]
    start = data.find('Contributors to this translation')
    pers = re.findall('class="sprite person">(.*?)</a>', data[start:])
    print '\n[%s] %s' % (lang, language)
    #f = codecs.open('TRANSLATORS', 'a', 'utf-8')
    #f.write('[%s] %s \n' % (lang, language))
    #f.close()
    for per in pers:
       print '     %s' % per
       #f = codecs.open('TRANSLATORS', 'a', 'utf-8')
       #f.write('     %s \n' % per)
       #f.close()
