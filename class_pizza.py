# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:48:20 2018

@author: César
"""

class Part:
    
    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y2 = y1
        

class Pizza:
    
    def __init__(self):
        self.listPart = []
        
    def slicep(self, pizza,x,y,x1,y1):
        if x1 >= len(pizza) or y >= len(pizza[0]):
            return False
        if x < 0 or y < 0:
            return False
        newPart = Part.part(x,y,x1,y1)
        if not self.checkIfThePartIsAlreadyTaken(newPart):
            self.listPart.append(newPart)
        return True
    
    def checkIfThePartIsAlreadyTaken(self,Part):
        return False
        