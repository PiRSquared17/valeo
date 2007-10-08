# -*- coding: utf-8 -*-
"""special wikiatividade from pt.wikipedia.org""" 
from glob import glob
from os.path import getsize
fn = raw_input('Filename: ')
arq = glob(fn)
tam = 0
for arqv in arq:
    tam += getsize(arqv)
print '%s bytes' % tam
raw_input()
