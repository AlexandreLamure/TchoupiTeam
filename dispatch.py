from class_ride import *
from class_car import *


def dst(x0, y0, x1, y1):
        return  abs(y1 - y0) + abs(x1 - x0)


def best_ride(car, rides):
    res = 0
    g = 
    l = 0
    for i in range(0, len(rides)):
        if rides[i].finished:
            continue
        dist = rides[i].distanceToStart(car)
        dist2 = rides[i].early - car.step

        if dist2 - dist == 0:
            return i

        elif dist2 - dist < 0:
            if 
            if rides[i].early < car.step:
                if rides[i].early < rides[g].early:
                    g = i


            


