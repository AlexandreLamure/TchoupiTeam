from class_pizza import *
data = Pizza()

def dumb_1(width, height, minimum, area, pizza):
    for y in range(0, len(pizza)):
        for x in range(0, len(pizza[0])):
            data.slicep(pizza, x, y, area, 1)
    data.save()
