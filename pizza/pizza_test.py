from class_pizza import *
from dumb_1 import *
from pizza_generator import *

import sys

def launch_test():
  if len(sys.argv) != 2:
    sys.exit()
  n = int(sys.argv[1])
  for i in range(0, n):
    r, c, l, h, tab = new_pizza()
    dumb_1(r, c, l , h,)