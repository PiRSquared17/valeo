#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO:
* i18n with gettext
* refresh button
* preferences dialog
* logo
* create MVC
* check internet
* check pygtk/gtk version installed
"""

name = 'Coopera Weather'
comments = 'Weather in your city'
copyright = '© Leonardo Gregianin, 2007'
website = 'http://code.google.com/p/valeo/wiki/CooperaWeather'

# version counting ;-)
import math
last_version = 0.17
current_version='%s'%(last_version*math.pi)

# License
GPL = '''"Coopera Weather is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Coopera Weather is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Coopera Weather; if not, write to the Free Software Foundation, Inc.,
51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA"
'''

from BeautifulSoup import *
from urllib import *
import gtk
import sys
import webbrowser
from code_city import code

# Mozilla Firefox for open weather.com
class Firefox(URLopener):
    version = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20061201 Firefox/2.0.0.3 (Ubuntu-feisty)"
    def __init__(self, *args):
        URLopener.__init__(self)
_urlopener = Firefox()

##############################################################
##############################################################
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
##############################################################
##############################################################

# Create menu in tray icon
class WeatherIcon(gtk.StatusIcon):

    def __init__(self):
        gtk.StatusIcon.__init__(self)
        menu = '''
               <ui>
               <menubar name="Menubar">
               <menu action="Menu">
               <menuitem action="City"/>
               <separator/>
               <menuitem action="Weather"/>
               <menuitem action="Temp"/>
               <menuitem action="Updated"/>
               <menuitem action="More information"/>
               <separator/>
               <menuitem action="Refresh"/>
               <menuitem action="Preferences"/>
               <separator/>
               <menuitem action="About"/>
               <menuitem action="Quit"/>
               </menu>
               </menubar>
               </ui>
               '''
        actions = [
            ('Menu',  None, 'Menu'),
            ('City', gtk.STOCK_YES, code.keys()[i], None, 'City', None),
            ('Weather', gtk.STOCK_YES, weather_c, None, 'Weather', None),
            ('Temp', gtk.STOCK_YES, temp, None, 'Temperature', None),
            ('Updated', gtk.STOCK_YES, updated, None, 'Updated', None),
            ('More information', gtk.STOCK_INFO, '_More information', None, 'More info', self.on_moreinfo),
            ('Refresh', gtk.STOCK_REFRESH, '_Refresh', None, 'Refresh weather', self.on_refresh),
            ('Preferences', gtk.STOCK_PREFERENCES, '_Preferences', None, 'Change City', self.on_preferences),
            ('About', gtk.STOCK_ABOUT, '_About', None, 'About Coopera Weather', self.on_about),
            ('Quit', gtk.STOCK_QUIT, '_Quit', None, 'Quit Coopera Weather', self.on_quit)]

        ag = gtk.ActionGroup('Actions')
        ag.add_actions(actions)
        self.manager = gtk.UIManager()
        self.manager.insert_action_group(ag, 0)
        self.manager.add_ui_from_string(menu)
        self.menu = self.manager.get_widget('/Menubar/Menu/About').props.parent
        self.set_from_stock(gtk.STOCK_YES)
        self.set_tooltip(name)
        self.set_visible(True)
        self.connect('popup-menu', self.on_popup_menu)
        
    def on_refresh(self, data):
        pass

    def on_preferences(self, data):
        pass
        
    def on_moreinfo(self, data):
        webbrowser.open(url)
        
    def on_quit(self, data):
        sys.exit()

    def on_popup_menu(self, status, button, time):
        self.menu.popup(None, None, None, button, time)

    def on_about(self, data):
        dialog = gtk.AboutDialog()
        dialog.set_name(name)
        dialog.set_version(current_version[:4])
        dialog.set_comments(comments)
        dialog.set_copyright(copyright)
        dialog.set_license(GPL)
        dialog.set_website(website)
        dialog.run()
        dialog.destroy()

# Create menu if internet not available
class OfflineIcon(gtk.StatusIcon):

    def __init__(self):
        gtk.StatusIcon.__init__(self)
        menu = '''
               <ui>
               <menubar name="Menubar">
               <menu action="Menu">
               <menuitem action="net"/>
               <separator/>
               <menuitem action="About"/>
               <menuitem action="Quit"/>
               </menu>
               </menubar>
               </ui>
               '''
        actions = [
            ('Menu',  None, 'Menu'),
            ('net', gtk.STOCK_NO, 'Internet not available', None, 'Internet', None),
            ('About', gtk.STOCK_ABOUT, '_About', None, 'About Coopera Weather', self.on_about),
            ('Quit', gtk.STOCK_QUIT, '_Quit', None, 'Quit Coopera Weather', self.on_quit)]

        ag = gtk.ActionGroup('Actions')
        ag.add_actions(actions)
        self.manager = gtk.UIManager()
        self.manager.insert_action_group(ag, 0)
        self.manager.add_ui_from_string(menu)
        self.menu = self.manager.get_widget('/Menubar/Menu/About').props.parent
        self.set_from_stock(gtk.STOCK_NO)
        self.set_tooltip(name)
        self.set_visible(True)
        self.connect('popup-menu', self.on_popup_menu)
        
    def on_quit(self):
        sys.exit()

    def on_popup_menu(self, status, button, time):
        self.menu.popup(None, None, None, button, time)

    def on_about(self):
        dialog = gtk.AboutDialog()
        dialog.set_name(name)
        dialog.set_version(current_version[:4])
        dialog.set_comments(comments)
        dialog.set_copyright(copyright)
        dialog.set_license(GPL)
        dialog.set_website(website)
        dialog.run()
        dialog.destroy()

if __name__ == '__main__':

    # Check if internet connect
    #try:
    WeatherIcon()
    gtk.main()
    #except:
    #    OfflineIcon()
    #    gtk.main()
