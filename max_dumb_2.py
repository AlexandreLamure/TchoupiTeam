from class_pizza import *
data = Pizza()

def get_tuples(minimum, area):

    arr = []
    for i in range(1, int(area / 2) + 1):
        for j in range(i, int(area / 2) + 1):
            if i * j >= minimum * 2 and i * j <= area:
                arr.append((i, j))
    return arr         

def get_best(arr, width, height):
    score = width % arr[0][0] == 0 + width % arr[0][1] == 0
    best = arr[0]
    for i in arr:
        s = width % i[0] == 0 + width % i[1] == 0
        if (s > score):
            best = i
            score = s
    return best


def max_dumb_2(width, height, minimum, area, pizza):

    arr = get_tuples(minimum, area)
    sl = get_best(arr, width, height)
    for y in range(0, len(pizza)):
        for x in range(0, len(pizza[0])):
            data.slicep(pizza, x, y, sl[0], sl[1])
    data.save()
