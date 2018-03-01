from class_ride import *
from class_car import *


def dst(x0, y0, x1, y1):
        return  abs(y1 - y0) + abs(x1 - x0)

def find_first(rides):
    i = 0
    l = len(rides)
    while (i < l and rides[i].finished == True):
        i += 1
    return i

def best_ride(car, rides):
    
    index = find_first(rides)
    if (index == len(rides)):
        return -1
    score = rides[index].early - car.step - rides[index].distanceToStart(car)

    for i in range(1, len(rides)):
        if rides[i].finished:
            continue
        dist = rides[i].distanceToStart(car)
        time = rides[i].early - car.step

        if time == dist:
            return i

        elif dist < time:
            if score < 0 or score > time - dist:
                index = i
                score = time - dist
        elif score < time - dist:
            index = i
            score = time - dist
    return index
            


