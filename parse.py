import sys
import os

def getfile():
    if len(sys.argv) != 2:
        sys.exit()
    filein = sys.argv[1]

    file  = open(filein, "r")
    i = 0
    tab = []
    for line in file:
        line = line[:-1]
        tab.append(line.split(' '))
        for n in range(len(tab[i])):
            tab[i][n] = int(tab[i][n])
        i += 1
    return tab[0], tab[1:]
