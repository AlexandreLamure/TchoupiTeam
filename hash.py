from parse import *
import time
import os
param, courses = getfile()

r, c, f, n, b, t = param

if not os.path.exists("results"):
    os.makedirs("results")
fichier = open("results/result_"+ str(time.time())+ "_"+str(0)+".txt","w")


for i in range(0, n):
    x0, y0, x1, y1, e, l = courses[i]
    rides.append(ride(x0, y0, x1, y1, e, l))

for i in range(0, f):
    cars.append(car())

# Main Loop
for i in range(0, t):
    dispatch()
    for car_tmp in cars:
        #move

'''
resp= str(n)
for i in range(n/f + 1):
    resp += ' ' + str(i)

for i in range(f - 1):
    resp += '\n0'
'''

for i in range(0, f):
    cars[i].rideToString()

fichier.write(resp)
fichier.close()

