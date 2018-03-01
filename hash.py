from parse import *
from class_ride import *
from class_car import *
import time
import os
from class_car import *

param, courses = getfile()
r, c, f, n, b, t = param

rides = []
for i in courses:
    rides.append(Ride(i[0],i[1],i[2],i[3],i[4],i[5]))

def dst(x0, y0, x1, y1):
    return  abs(y1 - y0) + abs(x1 - x0)

cars = []
for i in range(f):
    cars.append(car())

def get_first_car(cars):
    car = cars[0]
    for i in cars:
        if car.step > i.step:
            car = i
    return car

def has_courses(rides):
    i = 0
    l = len(rides)
    while (i < l and rides[i].finished == True):
        i += 1
    return i != l
    
while (has_courses(rides)):
    car = get_first_car(cars)
    ride = best_ride(car, rides)
    car.take_course(ride, rides)
    

resp = ''
for i in range(0, f):
    cars[i].rideToString()
    resp += '\n'
    
if not os.path.exists("results"):
    os.makedirs("results")
fichier = open("results/result_"+ str(time.time())+ "_"+str(0)+".txt","w")
resp = resp[:-1]
fichier.write(resp)
fichier.close()


