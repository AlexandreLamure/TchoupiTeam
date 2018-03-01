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
