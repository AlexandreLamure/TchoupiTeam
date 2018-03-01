from parse import *
import time
import os
param, courses = getfile()

r, c, f, n, b, t = param

if not os.path.exists("results"):
    os.makedirs("results")
fichier = open("results/result_"+ str(time.time())+ "_"+str(0)+".txt","w")

resp= str(n)
for i in range(n/f + 1):
    resp += ' ' + str(i)

for i in range(f - 1):
    resp += '\n0'
fichier.write(resp)
fichier.close()
