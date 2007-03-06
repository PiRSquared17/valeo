# -*- coding: utf-8 -*-
import wikipedia, gui, sys
try:
    lang = sys.argv[1]
    fam = sys.argv[2]
    art = wikipedia.input('Page:')
    site = wikipedia.getSite(lang, fam)
    page = wikipedia.Page(site, art)
    text = page.get()
    myapp = gui.EditBoxWindow()
    myapp.edit(text)
except:
    print 'use: %s en wikipedia' % sys.argv[0]