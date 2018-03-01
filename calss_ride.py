# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:12:48 2018

@author: César
"""

from math import sqrt

class Ride:
    def __init__(self, x0, y0, x1, y1):
        self.x0_ = x0
        self.y0_ = y0
        self.x1_ = x1
        self.y1_ = y1
        self.distance = sqrt((y1 - y0)**2 + (x1 - x0)**2)
