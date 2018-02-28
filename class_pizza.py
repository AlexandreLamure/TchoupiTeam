# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:48:20 2018

@author: César
"""
import time
import os

class Part:
    
    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        

class Pizza:
    
    def __init__(self):
        self.listPart = []
        
    def slicep(self, pizza,x,y,x1,y1):
        if x1 >= len(pizza) or y >= len(pizza[0]):
            return False
        if x < 0 or y < 0:
            return False
        newPart = Part(x,y,x1,y1)
        if not self.checkIfThePartIsAlreadyTaken(newPart):
            self.listPart.append(newPart)
        return True
    
    def checkIfThePartIsAlreadyTaken(self,partofPizza):
        for i in self.listPart:
            if partofPizza.x0 >= i.x0 and partofPizza.x0 <= i.x1 and partofPizza.y0 >=i.y0 and partofPizza.y0 <= i.y1:
                return False
            if partofPizza.x1 >= i.x0 and partofPizza.x1 <= i.x1 and partofPizza.y1 >=i.y0 and partofPizza.y1 <= i.y1:
                return False
        return True
    
    def Save(self):
        returnString = ""
        returnString += str(len(self.listPart)) +"\n"
        for i in self.listPart:
            returnString += i.x0 + " " + i.y0 + " " + i.x1 + " " + i.y1 + "\n"

        if not os.path.exists("results"):
            os.makedirs("results")
        fichier = open("results/result_"+ str(time.time())+ "_"+str(0)+".txt","w")
        fichier.write(returnString)
        fichier.close();
        return None
