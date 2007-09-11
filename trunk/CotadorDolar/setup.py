# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'Cotador Dolar',
    version = '0.1',
    description = u'Cotação do dólar direto do site do Banco Central do Brasil',
    author = 'Leonardo Gregianin',
    author_email = 'leogregianin@gmail.com',
    url = 'http://code.google.com/p/valeo/wiki/CotadroDolar',
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
    
    packages = ['CotadorDolar']
    )    
