
from Tkinter import Tk, PhotoImage, Button
from httplib import HTTPConnection

root = Tk()
headers = {'Accept': 'image/gif'}
conn = HTTPConnection('www.python.org')
conn.request('GET', '/images/python-logo.gif', None, headers)
r = conn.getresponse()
data = r.read()
arq = open('python-logo.gif','wb')
arq.write(data)
arq.close()
conn.close()
iconImage = PhotoImage(master=root, file='python-logo.gif')
Button(image=iconImage).pack()
