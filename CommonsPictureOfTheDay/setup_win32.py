# -*- coding: utf-8 -*-

## python setup_win32.py install

from distutils.core import setup
from _winreg import *
import os

setup(
    name = 'CommonsPictureOfTheDay',
    version = '1.0',
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

### Install CommonsPictureOfTheDay in registry
os.system('copy CommonsPictureOfTheDay\\CommonsPictureOfTheDay-Win32.pyw C:\\Python25\\Lib\\site-packages\\CommonsPictureOfTheDay\\')
Reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
Key = OpenKey(Reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
try:
    SetValueEx(Key,"CommonsPictureOfTheDay", 0, REG_SZ, r"C:\Python25\Lib\site-packages\CommonsPictureOfTheDay\CommonsPictureOfTheDay-Win32.pyw")
    print "\nCommonsPictureOfTheDay installed sucessful!"
except EnvironmentError:
    print "Encountered problems writing into the Registry..."
CloseKey(Key)
CloseKey(Reg)
