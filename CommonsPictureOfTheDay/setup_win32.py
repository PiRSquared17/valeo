# -*- coding: utf-8 -*-

## python setup_win32.py install

from distutils.core import setup
from _winreg import *
import os

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
    data_files=[('\\Lib\\site-packages\\pywikipedia', ['pywikipedia\\CommonsPictureOfTheDay-Win32.pyw'])]
    )    

### Install CommonsPictureOfTheDay in registry
os.system('copy pywikipedia\\CommonsPictureOfTheDay-Win32.pyw C:\\Python25\\Lib\\site-packages\\pywikipedia\\')
Reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
Key = OpenKey(Reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
try:
    SetValueEx(Key,"CommonsPictureOfTheDay", 0, REG_SZ, r"C:\Python25\Lib\site-packages\pywikipedia\CommonsPictureOfTheDay-Win32.pyw")
    print "\nCommons Picture Of The Day installed sucessful!"
except EnvironmentError:
    print "Encountered problems writing into the Registry..."
CloseKey(Key)
CloseKey(Reg)
