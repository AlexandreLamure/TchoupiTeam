from class_pizza import *
from parsing import *

w, h, mini, area, pizza = start()
data = Pizza(w, h, mini, area, pizza)

def get_tuples():

    arr = []
    for i in range(1, int(data.area / 2) + 1):
        for j in range(i, int(data.area / 2) + 1):
            if i * j >= data.mini * 2 and i * j <= data.area:
                arr.append((i, j))
    return arr         

def get_best(arr):
    score = data.w % arr[0][0] == 0 + data.h % arr[0][1] == 0
    best = arr[0]
    for i in arr:
        s = data.w % i[0] == 0 + data.h % i[1] == 0
        if (s > score):
            best = i
            score = s
    return best


def max_dumb_2():

    arr = get_tuples()
    sl = get_best(arr)
    for y in range(0, len(data.pizza)):
        for x in range(0, len(data.pizza[0])):
            print(x, y, x + sl[0], y + sl[1])
            data.slicep(data.pizza, x, y, x + sl[0], y + sl[1])
    data.Save()

max_dumb_2()
