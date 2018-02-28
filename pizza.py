from pizza import *

width, height, minimum, area, pizza = start()

def dumb_1():
    for y in range(0, len(pizza)):
        for x in range(0, len(pizza[0])):
            slicep(pizza, x, y, area, 1)
    save()
