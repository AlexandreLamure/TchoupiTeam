from parse import *
import time
import os
param, courses = getfile()

r, c, f, n, b, t = param

cours = []
x = 0
for i in courses:
    
    cours.append((x, i[4]))
    x += 1
cours = sorted(cours, key=lambda x: x[1])

if not os.path.exists("results"):
    os.makedirs("results")
fichier = open("results/result_"+ str(time.time())+ "_"+str(0)+".txt","w")

cars = []
for i in range(f):
    cars.append([0])

car = 0
index = 0
while (index < n):
    if (car >= f):
        car = 0
    cars[car].append(cours[index][0])
    cars[car][0] += 1
    car += 1
    index += 1

resp = ''
for i in cars:
    for j in i:
        resp += str(j) + ' '
    resp = resp[:-1]
    resp += '\n'

resp = resp[:-1]
fichier.write(resp)
fichier.close()
