# -*- coding: utf-8  -*-
"""
TEORIA:

valor for valor in iteração if comparação

lista = []
for valor in iteração:
     if comparação:
        lista.append(valor)
"""


# primeiro

lista = [[1,2,3], [4,5,6], [7,8,9]]
print [[r[col] for r in lista] for col in range(len(lista[0]))]


# segundo
# teoria:
#
# lista = []
# for letra in d:
#     if d[letra]/2 ==0:
#         lista.append(d[letra])

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
print [d[letra] for letra in d if d[letra]/2 <> 0]


# terceiro
# teoria:
#
# lista = []
# for letra in d:
#     if d[letra]/2 ==0:
#         lista.append(math.sqrt(d[letra]))

import math
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
print [math.sqrt(d[letra]) for letra in d if d[letra]/2 <> 0]
