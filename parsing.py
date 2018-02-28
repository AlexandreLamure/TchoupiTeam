# -*- coding: utf-8 -*-
### Google Hash code 2018
### BELLEY César, LAMURE Alexandre, LEE Sangbin, L'HERMITE Maxime.
###
###
import sys

def getfile():
    if len(sys.argv) != 3:
        sys.exit()
    filein = sys.argv[1]
    fileout = sys.argv[2]
    tab = []
    file  = open(filein, "r")
    i = 0
    for line in file:
        tab.append([])
        j = 0
        for char in line:
            if char != '\n' and char != '\r':
                tab[i].append(char)
            j += 1
        i += 1
    file.close() 
    param = tab[0]
    tab = tab[1:]
    return param, tab

def start():     
    param, pizza = getfile()
    words = ''.join(param).split(' ')
    return int(words[0]), int(words[1]), int(words[2]), int(words[3]), pizza



