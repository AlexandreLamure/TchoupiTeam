from parse import *
from class_ride import *
from class_car import *
import time
import os
from class_car import *
from dispatch import *

param, courses = getfile()
r, c, f, n, b, t = param

rides = []
x = 0
for i in courses:
    rides.append(Ride(i[0],i[1],i[2],i[3],i[4],i[5], x))
    x += 1

def dst(x0, y0, x1, y1):
    return  abs(y1 - y0) + abs(x1 - x0)

cars = []
for i in range(f):
    cars.append(Car())

cr = 0
while (len(rides) != 0):
    if (cr >= len(cars)):
        cr = 0
    car = cars[cr]
    ride = best_ride(car, rides)
    car.take_course(ride, rides)
    cr += 1

resp = ''
for i in range(0, f):
    resp += cars[i].rideToString()
    resp += '\n'
    
if not os.path.exists("results"):
    os.makedirs("results")
fichier = open("results/result_"+ str(time.time())+ "_"+str(0)+".txt","w")
resp = resp[:-1]
fichier.write(resp)
fichier.close()


