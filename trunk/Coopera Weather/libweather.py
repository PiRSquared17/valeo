#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import *
from urllib import *

from code_city import code

# Mozilla Firefox for open weather.com
class Firefox(URLopener):
    version = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20061201 Firefox/2.0.0.3 (Ubuntu-feisty)"
    def __init__(self, *args):
        URLopener.__init__(self)
_urlopener = Firefox()


i = 0
city = code.values()[i]
print city
print code.keys()[i]

url = 'http://www.weather.com/outlook/travel/businesstraveler/local/%s' % city
html = urlopen(url).read()
soup = BeautifulSoup(html)

weather = soup.find('strong', {'class': 'obsTextA'}).string
weather_c = 'Weather: %s' % weather
temperature = soup.find('strong', {'class':'obsTempTextA'}).string
temperature_split = int(temperature.replace(u'&deg;F', u''))
temperature_F2C = int(temperature_split-32)/1.8
temp_subst = temperature.replace(u'&deg;', u'º') # HTML string to unicode º
temp = '%s / %iºC' % (temp_subst, temperature_F2C)
updated = soup.find('div', {'class':'updated'}).string
