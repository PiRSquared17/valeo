# -*- coding: cp1252 -*-

import fbconsole as F
from time import sleep

#postar mensagem
"""
F.authenticate()
F.AUTH_SCOPE = ['friends_status']
while 1:
    F.post('/100000267867345/feed', {'message':u'Parabéns amor'})
    sleep(60*2)
"""

#postar foto
F.authenticate()
F.AUTH_SCOPE = ['publish_stream']
while 1:
    image = open("flor.jpg", "rb")
    photo_id = F.post('/100000267867345/photos',
                     {'name': u'testé,
                      'source': image})['id']
    sleep(60*2)
