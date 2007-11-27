# -*- coding: utf-8 -*-
from random import choice
from string import letters, digits, join

def random(tamanho=8, char=letters+digits):
    novo = []
    for i in range(tamanho):
        novo.append(choice(char))
    return join(novo,'')

if __name__ == "__main__":
    for i in range(15):
        print random(8, digits+letters)
