# -*- coding: utf-8 -*-
"""
Text file manipulation.

TODO:
   - codificação
   - replace wikipedia-like --> "# Saturno (inclusão)" to "* [[Saturno]]"
   - ordenação de linhas
   - incluir argumentos via linha-de-comando
   - orientação a objeto
   - BUG: tamanho do diretório

"""

from linecache import getline
from glob import glob
import sys, os

def countword(filename):
    #TODO: not_include = ['#', '-*-', '=', '%']
    word = filename.read().split()
    onlyw = set(word)
    print ('%d words, not repeat %d') % (len(word), len(onlyw))
    
def readline(filename):
    #print ('file %s was %d lines' % filename, linefile)
    line = input('What line do you want to see: ')
    theline = getline(filename, line)
    print theline

def removeline(filename):
    stext = raw_input('Search text: ')
    fil = open(filename, 'r')
    lines = fil.readlines()
    fil.close()
    for line in lines:
        if stext in line:
            count = lines.remove(line)
    fil = open(filename, 'w')
    fil.writelines(lines)
    fil.close()
    print ('All lines with %s, deleted!' % stext)

def replace(filename, filename2):
    all = 200000
    stext = raw_input('search text: ')
    rtext = raw_input('replace text: ')
    fil = open(filename, 'r')
    readl = fil.xreadlines()
    readl2 = open(filename2, 'w')
    for s in readl:
        readl2.write(s.replace(stext, rtext))
    readl.close()
    readl2.close()

def change_encoding(filename):
    pass

def filesize(fn):
    arq = glob(fn)
    tam = 0
    for arqv in arq:
        tam += os.path.getsize(arqv)
    tamMB = tam/1024.00
    print '%s bytes' % tam
    print '%s MB' % tamMB

def dirsize(fn):
    arq = glob(fn)
    tam = 0
    for arqv in arq:
        tam += os.path.getsize(arqv)
    tamMB = tam/1024.00
    print '%s bytes' % tam
    print '%s MB' % tamMB
   
def replacewikipedia(filename, filename2):
    fil = open(filename, 'r')
    readl = fil.xreadlines()
    readl2 = open(filename2, 'w')
    for line in readl.split('\n'):
        if '(inclusão)' in line:
            readl2.write(line.replace('(inclusão)', ''))
    readl.close()
    readl2.close()

def alphabetic_list(filename):
    line_start = input('a partir de qual linha quer ordenar: ')
    line_finish = input('até que linha: ')
    linesr = getline(filename, line_start)
    linefr = getline(filename, line_finish)
    print linesr, linefr
    line_between = (line_start - line_finish)
    between = getline(filename, line_between)
    print between

def main():
    print ("""* (c)ount word in file
* count (b)ytes in file or path
* (r)eadline in file 
* r(e)move line in file
* rep(l)ace text
* replace bra(k)ets links in file (wikipedia).
* replace enco(d)ing text of the file.
* (o)rdenar por linha a lista.""")

    choice = raw_input('What do you do: ')
    if choice == 'c':
        filename = file(raw_input('Filename: '))
        countword(filename)
    elif choice == 'r':
        filename = raw_input('Filename: ')
        readline(filename)
    elif choice == 'e':
        filename = raw_input('Filename: ')
        removeline(filename)
    elif choice == 'l':
        filename = raw_input('Filename root: ')
        filename2 = raw_input('Filename result: ')
        replace(filename, filename2)
    elif choice == 'd':
        filename = raw_input('Filename: ')
        change_encoding(filename)
    elif choice == 'k':
        filename = raw_input('Filename root: ')
        filename2 = raw_input('Filename result: ')
        replacewikipedia(filename, filename2)
    elif choice == 'b':
        choicebytes = raw_input('(f)ilename or (p)ath: ')
        if choicebytes == 'f':
            filename = raw_input('Filename: ')
            filesize(filename)
        elif choicebytes == 'p':
            pathname = raw_input('Path name: ')
            path = ('%s\*.*' % pathname)
            dirsize(path)
        else:
            print 'choose valid option'
    elif choice == 'o':
        filename = raw_input('Filename: ')
        alphabetic_list(filename)
    else:
        print __doc__
        if sys.platform=='win32':
            raw_input()
        
if __name__ == '__main__':
    main()
