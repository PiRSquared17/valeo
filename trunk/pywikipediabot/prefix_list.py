# -*- coding: utf-8 -*-
import wikipedia, pagegenerators, codecs

prefix = '' # your prefix
gen = pagegenerators.PrefixingPageGenerator(prefix)
preloadingGen = pagegenerators.PreloadingGenerator(gen)
for page in preloadingGen:
    pageprefix = page.title()
    if not page.isRedirectPage():
        f = codecs.open('ficheiro.txt', 'a', 'utf-8')
        f.write('# [[%s]]\n'% pageprefix)
        f.close()
