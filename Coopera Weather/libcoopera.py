#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import *
from urllib import *
import gtk
import sys, os
import webbrowser
from CodeCity import code
from FirefoxHeader import *

class About(gtk.AboutDialog):
    
    def __init__(self):
        super(About, self).__init__()
        self.set_name('Coopera Weather')
        self.set_comments('Current weather information from weather.com')
        self.set_version('0.17')
        self.set_copyright('© Leonardo Gregianin, 2007')
        self.set_license(file(os.path.join("", "LICENSE"), "r").read())
        self.set_website('http://code.google.com/p/cooperaweather')
        self.set_website_label('Coopera Weather website')
        self.set_authors([file(os.path.join("", "AUTHORS"), "r").read()])
        self.set_translator_credits(file(os.path.join("", "TRANSLATORS"), "r").read())
        self.set_artists([file(os.path.join("", "ARTISTS"), "r").read()])
        self.set_logo(gtk.gdk.pixbuf_new_from_file(os.path.join('files', 'weather-storm-logo.png')))
        self.set_modal(True)
        self.show_all()
        self.run()
        self.destroy()

class ExpanderCity(gtk.Dialog):

    def __init__(self, parent=None):
        gtk.Dialog.__init__(self, 'Choose your city', parent,  0, (gtk.STOCK_CLOSE, gtk.RESPONSE_NONE))
        self.connect("response", lambda d, r: d.destroy())
        self.set_resizable(False)

        vbox = gtk.VBox(False, 12)
        self.vbox.pack_start(vbox, True, True, 0)
        self.set_default_size(200, 200)
        vbox.set_border_width(8)

        label = gtk.Label()
        label.set_markup("Navegation for the expansion buttons:")
        vbox.pack_start(label, False, False, 0)

        expander = gtk.Expander("America"); vbox.pack_start(expander, False, False, 0)
        expander2 = gtk.Expander("Europa"); vbox.pack_start(expander2, False, False, 0)

        label = gtk.Label("Cuiaba, Brazil"); expander.add(label)
        
        label2 = gtk.Label("Lisboa, Portugal"); expander2.add(label2)
        
        self.show_all()

class WeatherChannel(gtk.StatusIcon):

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
        from libweather import weather_c, temp, updated, i
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
        #trayicon = os.path.join('', 'weather-storm-trayicon.png')
        self.set_from_stock(gtk.STOCK_YES)
        self.set_tooltip('Coopera Weather')
        self.set_visible(True)
        self.connect('popup-menu', self.on_popup_menu)
        
    def on_refresh(self, data):
        pass

    def on_preferences(self, data):
        ExpanderCity()
        
    def on_moreinfo(self, data):
        webbrowser.open(url)
        
    def on_quit(self, data):
        sys.exit()

    def on_popup_menu(self, status, button, time):
        self.menu.popup(None, None, None, button, time)

    def on_about(self, data):
        About()

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
        self.set_tooltip('Coopera Weather')
        self.set_visible(True)
        self.connect('popup-menu', self.on_popup_menu)
        
    def on_quit(self, data):
        sys.exit()

    def on_popup_menu(self, status, button, time):
        self.menu.popup(None, None, None, button, time)

    def on_about(self, data):
        About()

