from class_pizza import *


def get_tuples(area):

    arr = []
    for i in range(1, area / 2 + 1):
        for j in range(i, area / 2 + 1):
            if i * j == area:
                arr.append(i, j)
    return arr
                

def max_dumb_2(width, height, minimum, area, pizza):

    arr = get_tuples(area)
    for i in arr:
        print(i)
    for y in range(0, len(pizza)):
        for x in range(0, len(pizza[0])):
            pizza.slicep(pizza, x, y, area, 1)
    pizza.save()
