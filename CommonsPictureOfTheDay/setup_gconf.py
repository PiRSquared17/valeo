# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'CommonsPictureOfTheDay',
    version = '0.1',
    description = 'Put "picture of the day" in your Desktop wallpaper from Wikimedia Commons',
    author = 'Leonardo Gregianin',
    author_email = 'leogregianin@gmail.com',
    url = 'http://code.google.com/p/valeo/wiki/CommonsPictureOfTheDay',
    download_url = 'http://code.google.com/p/valeo/downloads/list',
    license = 'MIT',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
    
    packages = ['pywikipedia', 'pywikipedia.families', 'pywikipedia.userinterfaces'],
    )

## python setup.py install

# TODO:
# create nautilus-python entry:
#   desktop -> preferences -> sessions ->
#      startup programs -> add ->
#          /usr/lib/python2.5/site-packages/CommonsPictureOfTheDay/pywikipedia/CommonsPictureOfTheDay-Gconf.py
