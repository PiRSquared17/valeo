# -*- coding: utf-8 -*-
"""
0 = Black          1 = Blue            2 = Green
3 = Aqua           4 = Red             5 = Purple
6 = Yellow         7 = White           8 = Gray
9 = Light Blue     10 = Light Green    11 = Light Aqua
12 = Light Red     13 = Light Purple   14 = Light Yellow

Este código é baseado no software Python Wikipedia Bot, distribuído pela MIT license.

"""
import ctypes, sys

def printColorizedInWindows(text, color):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    for i in range(0, len(color)):
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
        sys.stdout.write(text)
    # cor de fundo é 7
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    
if __name__ == "__main__":
    text = u"Imprimindo texto colorido no MS-DOS"
    color = [6] # número da cor do texto
    printColorizedInWindows(text, color)
