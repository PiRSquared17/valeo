# -*- coding: utf-8 -*-

## python setup.py install

from distutils.core import setup

setup(
    name = 'Wallpaper-commons',
    version = '0.0.1',
    description = 'Put "picture of the day" in your Desktop wallpaper from Wikimedia Commons',
    author = 'Leonardo Gregianin',
    author_email = 'leogregianin@gmail.com',
    url = 'http://code.google.com/p/wallpaper-commons',
    download_url = 'http://code.google.com/p/wallpaper-commons/downloads/list',
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

# create nautilus-python entry:
#   desktop -> preferences -> sessions ->
#      startup programs -> add -> /usr/lib/python2.5/site-packages/wallpaper-commons/pywikipedia/wallpaper-gconf.py
