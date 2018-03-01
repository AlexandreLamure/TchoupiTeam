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
    
    def rideTostring(self):
        chaine = ""
        for i in self.myCourse_:
            chaine += " " + str(i)
            return str(len(self.myCourse_)) + chaine 
        
    