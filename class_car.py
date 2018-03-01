# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:04:25 2018

@author: César
"""



class Car:
    def __init__(self):
        self.x_ = 0
        self.y_ = 0
        self.myCourse_ = []
        self.free_ = True
        self.distance_ = 0
        self.ride_ = None
    
    def rideTostring(self):
        chaine = ""
        for i in self.myCourse_:
            chaine += " " + str(i)
            return str(len(self.myCourse_)) + chaine 
        
    def move(self):
        if self.distance_ == 0:
            return False
        else:
            self.distance_ -= 1
            if self.distance_ == 0:
                if self.x_ == self.ride_.x0 and self.y_ == self.ride_.y0:
                    self.x_ = self.ride_.x0
                    self.y_ = self.ride_.y0
                elif self.x_ == self.ride_.x0 and self.y_ == self.ride_.y0:
                    self.x_ = self.ride_.x1
                    self.y_ = self.ride_.y1
                    self.free_ = True
                    self.ride_ = None
                return True