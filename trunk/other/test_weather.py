# -*- coding: utf-8 -*-
from BeautifulSoup import *
import urllib

# code your city
varzea_grande = "BRXX0255"
url = "http://www.weather.com/outlook/travel/businesstraveler/local/%s" % varzea_grande
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

weather = soup.find("strong", {"class":"obsTextA"}).string
print u"Weather: %s" % weather

temperature = soup.find("strong", {"class":"obsTempTextA"}).string
temperature_split = int(temperature.replace(u'&deg;F', u''))
temperature_F2C = (temperature_split-32)/1.8
# HTML string to unicode º
temp_subst = temperature.replace(u"&deg;", u"º")
print u"Temperature: %s or %sºC" % (temp_subst, int(temperature_F2C))

updated = soup.find("div", {"class":"updated"}).string
print updated
