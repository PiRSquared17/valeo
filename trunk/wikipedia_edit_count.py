# -*- coding: utf-8 -*-
import time
from urllib import urlopen

start=time.time() 
# Replication lag
replag = urlopen('http://tools.wikimedia.de/~interiot/cgi-bin/replag?text').read()
print replag

# Kate/Interiot's editcount
user = 'LeonardoG'
family = 'ptwiki_p'
site = ('http://tools.wikimedia.de/~river/cgi-bin/count_edits?user=%s&dbname=%s&machread=1' % (user, family))
getSite = urlopen(site).read()

for line in getSite.split('\n'):
    if 'TOTAL_EDITS' in line:
        li1 = line.replace('TOTAL_EDITS ', '')

for line in getSite.split('\n'):
    if 'DELETED_EDITS' in line:
        li2 = line.replace('DELETED_EDITS ', '')

x10 = (int(li1)+int(li2))
xx10 = (u'total de\n%s edições (edições válidas:%s + eliminadas:%s)' % (x10, li1, li2))

print ((u'%s na %s tem um %s') % (user, family, xx10))
end=time.time()
print (u'página gerada em %.3f seg' % (end-start))
