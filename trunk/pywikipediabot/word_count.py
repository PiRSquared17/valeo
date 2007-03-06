# -*- coding: utf-8 -*-
'''
Após a contagem de palavras é necessário apagar o conteúdo
do arquivo count-words.txt
'''
import wikipedia, pagegenerators, codecs

class CountWord:
    def count(self):
        site = wikipedia.getSite()
        page = wikipedia.input('Page:')
        pg = wikipedia.Page(site, page)
        pageget = pg.get()

        f = codecs.open('count-word.txt', 'a', 'utf-8')
        f.write(u'%s' % pageget)
        f.close()

        arq = file('count-word.txt')
        word = arq.read().split()
        print ('Words: %d' % (len(word)))

if __name__ == '__main__':
    c = CountWord()
    c.count()