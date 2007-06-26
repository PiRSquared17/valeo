# -*- coding: utf-8 -*-

## python setup_win32.py install

from distutils.core import setup
from _winreg import *
import os

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
    data_files=[('\\Lib\\site-packages\\pywikipedia', ['pywikipedia\\wallpaper-win32.pyw'])]
    )    

### Install wallpaper-commons in registry
os.system('copy pywikipedia\\wallpaper-win32.pyw C:\\Python25\\Lib\\site-packages\\pywikipedia\\')
Reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
Key = OpenKey(Reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
try:
    SetValueEx(Key,"Wallpaper-commons", 0, REG_SZ, r"C:\Python25\Lib\site-packages\pywikipedia\wallpaper-win32.pyw")
    print "\nWallpaper-commons installed sucessful!"
except EnvironmentError:
    print "Encountered problems writing into the Registry..."
CloseKey(Key)
CloseKey(Reg)
