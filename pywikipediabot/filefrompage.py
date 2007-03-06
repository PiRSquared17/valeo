#!/usr/bin/python
# -*- coding: utf-8  -*-
import wikipedia
import codecs
import pagegenerators

ensite = wikipedia.getSite()
listpageTitle = wikipedia.input('Page:')
listpage = wikipedia.Page(ensite, listpageTitle)
gen = pagegenerators.LinkedPageGenerator(listpage)
generator = pagegenerators.PreloadingGenerator(gen, pageNumber = [])
for page in generator:
    pagetitle = page.title()
    pagelist = page.get()
    f = codecs.open('ficheiro.txt', 'a', 'utf-8')
    f.write("""xxxx
    '''%s'''\n
    %s
    yyyy\n
    """ % (pagetitle, pagelist))
    f.close()
print 'save sucessful!'