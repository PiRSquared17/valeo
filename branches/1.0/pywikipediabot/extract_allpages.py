# -*- coding: utf-8 -*-

import wikipedia, pagegenerators
import time, codecs

def GenerateTitles():
    inicio = time.strftime('%H:%M:%S', time.localtime())
    allpages = '!'
    namespace = wikipedia.Page(wikipedia.getSite(), allpages).namespace()
    firstPageTitle = wikipedia.Page(wikipedia.getSite(), allpages).titleWithoutNamespace()
    gen = pagegenerators.AllpagesPageGenerator(allpages, namespace, includeredirects = False)
    preloadingGen = pagegenerators.PreloadingGenerator(gen)
    for page in preloadingGen:
        pagetitle = page.title()
        f = codecs.open('wiki-list.py', 'a', 'utf-8')
        f.write('%s\n' % pagetitle)
        f.close()
    fim = time.strftime('%H:%M:%S', time.localtime())
    wikipedia.output('Start: %s and finish %s' % (inicio, fim))
    
def PrintList():
    f = codecs.open('wiki-list.py', 'r', 'utf-8')
    text = f.read()
    i=1
    for list in text.split('\n'):
        if not list.startswith('#'):
            page = u'%s' % list
            print u'%i: %s' % (i, page)
            i+=1
        f.close()

def FindTitles():
    f = codecs.open('wiki-list.py', 'r', 'utf-8')
    text = f.read()
    i=1
    search = wikipedia.input(u'What article search:')
    for list in text.split('\n'):
        if not list.startswith('#'):
            if search in list:
                print u'Line %i, %s' % (i, list)
                i+=1
        f.close()

def menu():
    choice = wikipedia.input('1. Extract all pages from text file?\n2. Print list of title?\n3. Search title?\nOptions:')
    if choice == '1':
        GenerateTitles()
    elif choice == '2':
        PrintList()
    elif choice == '3':
        FindTitles()
    else:
        menu()    

if __name__ == '__main__':
    menu()
    
