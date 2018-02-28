from class_pizza import *

def dumb_1(width, height, minimum, area, pizza):
    for y in range(0, len(pizza)):
        for x in range(0, len(pizza[0])):
            slicep(pizza, x, y, area, 1)
    save()
