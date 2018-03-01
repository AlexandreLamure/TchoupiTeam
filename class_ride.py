# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:12:48 2018

@author: César
"""

from math import *

class Ride:
    def __init__(self, x0, y0, x1, y1, e, l, index):
        self.x0_ = x0
        self.y0_ = y0
        self.x1_ = x1
        self.y1_ = y1
        self.early = e
        self.last = l
        self.index = index
        self.distance = self.distancePoint(x0, y0, x1, y1)
        
    
    def search(self, rides, car, turn):
        distance = None
        index = None
        for i in range(0, len(rides)):
            test = self.distancePoint(self.x1_, self.y1_, rides[i].x0_, rides[i].y0_)
            if (distance == None or test < distance) and self.distanceToEnd(car) + test + turn <= rides[i].early:
                distance = self.distancePoint(self.x1_, self.y1_, rides[i].x0_, rides[i].y0_)
                index = i
        car.nextRide = rides[index]
        rides[index].early = 0
        return rides[index]
            


    def distancePoint(self, x0, y0, x1, y1):
        return  abs(y1 - y0) + abs(x1 - x0)
    
    def distanceToStart(self, car):
        return self.distancePoint(self.x0_, self.y0_, car.x_, car.y_)
    
    def distanceToEnd(self, car):
        return self.distance + self.distanceToStart(car)
    
    
    def checkRideValid(self, tour):
        if self.last < tour:
            self.finished = True
            return False
        else:
            return True
    
    def checkRide(self, tour, car):
        if self.last < self.distanceToEnd(car) + tour:
            return False
        else:
            return True
