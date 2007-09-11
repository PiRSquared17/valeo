# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'Frase do Dia',
    version = '0.1',
    description = u'Frase do Dia pelo site http://pt.wikiquote.org (projeto irmão da Wikipedia), requer Tkinter',
    author = 'Leonardo Gregianin',
    author_email = 'leogregianin@gmail.com',
    url = 'http://code.google.com/p/valeo/wiki/FrasedoDia',
    download_url = 'http://code.google.com/p/valeo/downloads/list',
    license = 'MIT',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
    
    packages = ['Frase do dia', 'Frase do dia.families', 'Frase do dia.userinterfaces'],
    )    
