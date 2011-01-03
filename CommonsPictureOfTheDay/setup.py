# -*- coding: utf-8 -*-

## python setup.py install

from distutils.core import setup
import os

setup(
    name = 'CommonsPictureOfTheDay',
    version = '1.1',
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
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
    
    packages = ['CommonsPictureOfTheDay', 'CommonsPictureOfTheDay.families', 'CommonsPictureOfTheDay.userinterfaces'],
    data_files=[('\\Python25\\Lib\\site-packages\\CommonsPictureOfTheDay', ['CommonsPictureOfTheDay\\CommonsPictureOfTheDay-Win32.pyw'])]
    )
