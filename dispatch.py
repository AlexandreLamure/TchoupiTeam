from class_ride import *
from class_car import *

def dispatch(cars, rides):
    for c in cars:
        if (c.free_):
            for i in range(0, len(rides)):
                if not rides[i].finished:
                    c.free_ = False
                    c.ride_ = rides[i]
                    break
            
