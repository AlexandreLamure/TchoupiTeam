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
        #self.free_ = True
        #self.distance_ = 0
        #self.waiting_ = True
        #self.ride_ = None
        self.step = 0
    
    def rideTostring(self):
        chaine = ""
        for i in self.myCourse_:
            chaine += " " + str(i)
            return str(len(self.myCourse_)) + chaine 
        
    def take_course(self, index, tabRides):
        self.x_ = tabRides[index].x1_
        self.y_ = tabRides[index].y1_
        self.myCourse_.append(index)
        self.step += tabRides[index].distanceToEnd(self)
        
        
        
        
    
"""
   def move(self, tour):
        if self.distance_ == 0:
            return self.timeTogo(self,tour)
        else:
            self.distance_ -= 1
            if self.distance_ == 0:
                if self.x_ == self.ride_.x0 and self.y_ == self.ride_.y0:
                    self.x_ = self.ride_.x0
                    self.y_ = self.ride_.y0
                    self.waiting_ = True
                elif self.x_ == self.ride_.x1 and self.y_ == self.ride_.y1:
                    self.x_ = self.ride_.x1
                    self.y_ = self.ride_.y1
                    self.free_ = True
                    self.ride_ = None
                    self.waiting_ = True
                return True
            
    def timeTogo(self,tour):
        if tour >= self.ride.early:
            self.distance = self.ride.distance-1
            return True
        else:
            return False
"""
    
    
